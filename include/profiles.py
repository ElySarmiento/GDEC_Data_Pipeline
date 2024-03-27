"Contains profile mappings used in the project"

from cosmos import ProfileConfig
from cosmos.profiles import SnowflakeUserPasswordProfileMapping


snowflake_trial = ProfileConfig(
    profile_name="snowflake_trial",
    target_name="dev",
    profile_mapping=SnowflakeUserPasswordProfileMapping(
        conn_id="snowflake_trial",
        profile_args={
            "database": "dbt_hol_dev",
            "schema": "public"
      },
    ),
)

snowflake_con = ProfileConfig(
    profile_name="snowflake_con",
    target_name="dev",
    profile_mapping=SnowflakeUserPasswordProfileMapping(
        conn_id="snowflake_con",
        profile_args={
            "database": "DEV_DB",
            "schema": "DEV_INTEG_SPE_SCH"
      },
    ),
)
