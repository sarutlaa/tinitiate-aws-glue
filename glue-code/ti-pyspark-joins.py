from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.dynamicframe import DynamicFrame

# Initialize Spark context with log level
sc = SparkContext.getOrCreate()  # Ensures that a Spark context is created only once
sc.setLogLevel("INFO")  # Setting log level for Spark context

glueContext = GlueContext(sc)

# Define Athena catalog and database
database = "glue_db"

# Load tables from Athena into DynamicFrames
product_dyf = glueContext.create_dynamic_frame.from_catalog(database=database, table_name="product")
category_dyf = glueContext.create_dynamic_frame.from_catalog(database=database, table_name="category")

# Convert DynamicFrames to DataFrames
product_df = product_dyf.toDF()
category_df = category_dyf.toDF()

# Select specific columns from the tables to avoid duplicate column names and perform renaming
product_selected_df = product_df.select("productid", "productname", "categoryid", "unit_price").withColumnRenamed("categoryid", "product_categoryid")
category_selected_df = category_df.select("categoryid", "categoryname")

# Perform various types of joins
joins = {
    "inner": product_selected_df.join(category_selected_df, product_selected_df["product_categoryid"] == category_selected_df["categoryid"], "inner"),
    "left_outer": product_selected_df.join(category_selected_df, product_selected_df["product_categoryid"] == category_selected_df["categoryid"], "left"),
    "right_outer": product_selected_df.join(category_selected_df, product_selected_df["product_categoryid"] == category_selected_df["categoryid"], "right"),
    "full_outer": product_selected_df.join(category_selected_df, product_selected_df["product_categoryid"] == category_selected_df["categoryid"], "outer"),
}

# Log the count of rows and show results for each join type
for join_type, df in joins.items():
    # Log the count of rows in the joined DataFrame
    glueContext.get_logger().info("Number of rows in the {0} joined DataFrame: {1}".format(join_type, df.count()))
    
    # Show the resulting DataFrame
    df.show()

    # Drop the category_categoryid column from the joined DataFrame
    df = df.drop("product_categoryid")
    
    # Show the resulting DataFrame after dropping the column
    df.show()
