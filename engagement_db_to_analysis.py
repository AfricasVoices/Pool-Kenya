import argparse
import importlib

from core_data_modules.logging import Logger

from src.engagement_db_to_analysis.engagement_db_to_analysis import generate_analysis_files

log = Logger(__name__)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Runs the engagement to analysis phases of the pipeline")

    parser.add_argument("--dry-run", action="store_true",
                        help="Logs the updates that would be made without updating anything.")
    parser.add_argument("--incremental-cache-path",
                        help="Path to a directory to use to cache results needed for incremental operation.")

    parser.add_argument("user", help="Identifier of the user launching this program")
    parser.add_argument("google_cloud_credentials_file_path", metavar="google-cloud-credentials-file-path",
                        help="Path to a Google Cloud service account credentials file to use to access the "
                             "credentials bucket"),
    parser.add_argument("configuration_module",
                        help="Configuration module to import e.g. 'configurations.test_config'. "
                             "This module must contain a PIPELINE_CONFIGURATION property")
    parser.add_argument("membership_group_dir_path",
                        help="Path to a directory to use to read & write membership group csvs to.")
    parser.add_argument("output_dir", metavar="output-dir",
                        help="Directory to output all analysis results to. This script will create and organise the "
                             "outputs into sensible sub-directories automatically")

    args = parser.parse_args()

    dry_run = args.dry_run
    incremental_cache_path = args.incremental_cache_path

    user = args.user
    google_cloud_credentials_file_path = args.google_cloud_credentials_file_path
    pipeline_config = importlib.import_module(args.configuration_module).PIPELINE_CONFIGURATION
    membership_group_dir_path = args.membership_group_dir_path
    output_dir = args.output_dir

    pipeline = pipeline_config.pipeline_name

    dry_run_text = "(dry run)" if dry_run else ""
    log.info(f"Running the engagement to analysis phases of the pipeline {dry_run_text}")

    uuid_table = pipeline_config.uuid_table.init_uuid_table_client(google_cloud_credentials_file_path)
    engagement_db = pipeline_config.engagement_database.init_engagement_db_client(google_cloud_credentials_file_path)

    if pipeline_config.rapid_pro_target is None:
        rapid_pro = None
    else:
        rapid_pro = pipeline_config.rapid_pro_target.rapid_pro.init_rapid_pro_client(google_cloud_credentials_file_path)

    if pipeline_config.analysis is None:
        log.info(f"No analysis configuration specified; exiting")
        exit(0)

    generate_analysis_files(user, google_cloud_credentials_file_path, pipeline_config, uuid_table, engagement_db, rapid_pro,
                            membership_group_dir_path, output_dir, incremental_cache_path, dry_run)
