##### initial setup:

import great_expectations as gx

context = gx.get_context(project_root_dir="./")

##### sources:

try:
    datasource = context.sources.get("my_postgres_db")
except KeyError:
    datasource = context.sources.add_postgres(
        name = "my_postgres_db",
        connection_string = "postgresql+psycopg2://lucasrangel:scrapyword@5432/scrapy_data"
    )

try:
    asset = datasource.get_asset("gx_stg_data")
except LookupError:
    datasource.add_table_asset(name="gx_stg_data", table="stg_data")

##### suites:

suite_name = "data_quality_suite"

try:
    suite = context.suites.get(suite_name)
except KeyError:
    suite = context.suites.add(gx.ExpectationSuite(name=suite_name))