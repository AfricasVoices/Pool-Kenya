from core_data_modules.cleaners import swahili

from src.pipeline_configuration_spec import *


def load_code_scheme(fname):
    with open(f"code_schemes/{fname}.json") as f:
        return CodeScheme.from_firebase_map(json.load(f))


rapid_pro_uuid_filter = UuidFilter(uuid_file_url="gs://avf-project-datasets/Test/2021/Kenya-Pool/opt_in_uuids.json")


PIPELINE_CONFIGURATION = PipelineConfiguration(
    pipeline_name="Create-Kenya-Pool",
    description="Creates the initial Kenya Pool from demographics responses to COVID19, COVID19-Ke-Urban, "
                "UNDP-Kenya, UNICEF-KENYA, OXFAM-KENYA, World Vision, and GPSDD.",
    engagement_database=EngagementDatabaseClientConfiguration(
        credentials_file_url="gs://avf-credentials/firebase-test.json",
        database_path="engagement_db_experiments/Kenya"
    ),
    uuid_table=UUIDTableClientConfiguration(
        credentials_file_url="gs://avf-credentials/avf-id-infrastructure-firebase-adminsdk-6xps8-b9173f2bfd.json",
        table_name="avf-global-urn-to-participant-uuid",
        uuid_prefix="avf-participant-uuid-"
    ),
    operations_dashboard=OperationsDashboardConfiguration(
        credentials_file_url="gs://avf-credentials/avf-dashboards-firebase-adminsdk-gvecb-ef772e79b6.json",
    ),
    rapid_pro_sources=[
        RapidProSource(
            rapid_pro=RapidProClientConfiguration(
                domain="textit.com",
                token_file_url="gs://avf-credentials/covid19-2-text-it-token.txt"
            ),
            sync_config=RapidProToEngagementDBConfiguration(
                flow_result_configurations=[
                    FlowResultConfiguration("covid19_ke_urban_s01_demog", "constituency", "kenya_pool_location"),
                    FlowResultConfiguration("covid19_ke_urban_s01_demog", "gender", "kenya_pool_gender"),
                    FlowResultConfiguration("covid19_ke_urban_s01_demog", "age", "kenya_pool_age"),

                    FlowResultConfiguration("undp_kenya_s01_demog", "constituency", "kenya_pool_location"),
                    FlowResultConfiguration("undp_kenya_s01_demog", "gender", "kenya_pool_gender"),
                    FlowResultConfiguration("undp_kenya_s01_demog", "age", "kenya_pool_age")
                ],
                uuid_filter=rapid_pro_uuid_filter
            )
        ),
        RapidProSource(
            rapid_pro=RapidProClientConfiguration(
                domain="textit.com",
                token_file_url="gs://avf-credentials/covid19-text-it-token.txt"
            ),
            sync_config=RapidProToEngagementDBConfiguration(
                flow_result_configurations=[
                    FlowResultConfiguration("covid19_s01_demog", "constituency", "kenya_pool_location"),
                    FlowResultConfiguration("covid19_s01_demog", "gender", "kenya_pool_gender"),
                    FlowResultConfiguration("covid19_s01_demog", "age", "kenya_pool_age"),
                ],
                uuid_filter=rapid_pro_uuid_filter
            )
        ),
        RapidProSource(
            rapid_pro=RapidProClientConfiguration(
                domain="textit.com",
                token_file_url="gs://avf-credentials/unicef-kenya-textit-token.txt"
            ),
            sync_config=RapidProToEngagementDBConfiguration(
                flow_result_configurations=[
                    FlowResultConfiguration("unicef_covid19_ke_s01_demog", "constituency", "kenya_pool_location"),
                    FlowResultConfiguration("unicef_covid19_ke_s01_demog", "gender", "kenya_pool_gender"),
                    FlowResultConfiguration("unicef_covid19_ke_s01_demog", "age", "kenya_pool_age"),
                ],
                uuid_filter=rapid_pro_uuid_filter
            )
        ),
        RapidProSource(
            rapid_pro=RapidProClientConfiguration(
                domain="textit.com",
                token_file_url="gs://avf-credentials/oxfam-kenya-textit-token.txt"
            ),
            sync_config=RapidProToEngagementDBConfiguration(
                flow_result_configurations=[
                    FlowResultConfiguration("oxfam_wash_s01_demog", "constituency", "kenya_pool_location"),
                    FlowResultConfiguration("oxfam_wash_s01_demog", "gender", "kenya_pool_gender"),
                    FlowResultConfiguration("oxfam_wash_s01_demog", "age", "kenya_pool_age"),
                    FlowResultConfiguration("oxfam_wash_s01_demog", "disabled", "kenya_pool_disabled"),
                ],
                uuid_filter=rapid_pro_uuid_filter
            )
        ),
        RapidProSource(
            rapid_pro=RapidProClientConfiguration(
                domain="textit.com",
                token_file_url="gs://avf-credentials/world-vision-textit-token.txt"
            ),
            sync_config=RapidProToEngagementDBConfiguration(
                flow_result_configurations=[
                    FlowResultConfiguration("worldvision_s01_demog", "constituency", "kenya_pool_location"),
                    FlowResultConfiguration("worldvision_s01_demog", "gender", "kenya_pool_gender"),
                    FlowResultConfiguration("worldvision_s01_demog", "age", "kenya_pool_age"),
                ],
                uuid_filter=rapid_pro_uuid_filter
            )
        ),
        RapidProSource(
            rapid_pro=RapidProClientConfiguration(
                domain="textit.com",
                token_file_url="gs://avf-credentials/gpsdd-kilifi-textit-token.txt"
            ),
            sync_config=RapidProToEngagementDBConfiguration(
                flow_result_configurations=[
                    FlowResultConfiguration("gpsdd_kilifi_s01_demog", "constituency", "kenya_pool_location"),
                    FlowResultConfiguration("gpsdd_kilifi_s01_demog", "gender", "kenya_pool_gender"),
                    FlowResultConfiguration("gpsdd_kilifi_s01_demog", "age", "kenya_pool_age"),
                    FlowResultConfiguration("gpsdd_kilifi_s01_demog", "disabled", "kenya_pool_disabled"),
                ],
                uuid_filter=rapid_pro_uuid_filter
            )
        ),
        RapidProSource(
            rapid_pro=RapidProClientConfiguration(
                domain="textit.com",
                token_file_url="gs://avf-credentials/gpsdd-kiambu-textit-token.txt"
            ),
            sync_config=RapidProToEngagementDBConfiguration(
                flow_result_configurations=[
                    FlowResultConfiguration("gpsdd_kiambu_s01_demog", "constituency", "kenya_pool_location"),
                    FlowResultConfiguration("gpsdd_kiambu_s01_demog", "gender", "kenya_pool_gender"),
                    FlowResultConfiguration("gpsdd_kiambu_s01_demog", "age", "kenya_pool_age"),
                    FlowResultConfiguration("gpsdd_kiambu_s01_demog", "disabled", "kenya_pool_disabled"),
                ],
                uuid_filter=rapid_pro_uuid_filter
            )
        ),
        RapidProSource(
            rapid_pro=RapidProClientConfiguration(
                domain="textit.com",
                token_file_url="gs://avf-credentials/gpsdd-bungoma-textit-token.txt"
            ),
            sync_config=RapidProToEngagementDBConfiguration(
                flow_result_configurations=[
                    FlowResultConfiguration("gpsdd_bungoma_s01_demog", "constituency", "kenya_pool_location"),
                    FlowResultConfiguration("gpsdd_bungoma_s01_demog", "gender", "kenya_pool_gender"),
                    FlowResultConfiguration("gpsdd_bungoma_s01_demog", "age", "kenya_pool_age"),
                    FlowResultConfiguration("gpsdd_bungoma_s01_demog", "disabled", "kenya_pool_disabled"),
                ],
                uuid_filter=rapid_pro_uuid_filter
            )
        )
    ],
    coda_sync=CodaConfiguration(
        coda=CodaClientConfiguration(credentials_file_url="gs://avf-credentials/coda-production.json"),
        sync_config=CodaSyncConfiguration(
            dataset_configurations=[
                CodaDatasetConfiguration(
                    coda_dataset_id="Kenya_Pool_location",
                    engagement_db_dataset="kenya_pool_location",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("kenya_constituency"), auto_coder=None),
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("kenya_county"), auto_coder=None)
                    ],
                    ws_code_string_value="location"
                ),
                CodaDatasetConfiguration(
                    coda_dataset_id="Kenya_Pool_gender",
                    engagement_db_dataset="kenya_pool_gender",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("gender"),
                                                auto_coder=swahili.DemographicCleaner.clean_gender)
                    ],
                    ws_code_string_value="gender"
                ),
                CodaDatasetConfiguration(
                    coda_dataset_id="Kenya_Pool_age",
                    engagement_db_dataset="kenya_pool_age",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("age"), auto_coder=lambda x:
                                                str(swahili.DemographicCleaner.clean_age_within_range(x)))
                    ],
                    ws_code_string_value="age"
                ),
                CodaDatasetConfiguration(
                    coda_dataset_id="Kenya_Pool_disabled",
                    engagement_db_dataset="kenya_pool_disabled",
                    code_scheme_configurations=[
                        CodeSchemeConfiguration(code_scheme=load_code_scheme("disabled"), auto_coder=None)
                    ],
                    ws_code_string_value="disabled"
                ),
            ],
            ws_correct_dataset_code_scheme=load_code_scheme("kenya_pool_ws_correct_dataset"),
            default_ws_dataset="kenya_pool_rqa"  # These can be manually archived later.
        )
    ),
)
