"""
URL configurations for the fEMR OnChain module.
"""
from django.conf.urls import include
from django.urls import path, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework import routers
from rest_framework.authtoken import views as rest_framework_views

from main.admin_views import (
    add_user_to_campaign,
    add_users_to_campaign,
    admin_home,
    create_user_view,
    cut_user_from_campaign,
    export_audit_logs_view,
    export_database_logs_view,
    filter_audit_logs_view,
    filter_database_logs_view,
    filter_users_view,
    get_audit_logs_view,
    get_database_logs_view,
    list_users_view,
    lock_user_view,
    message_of_the_day_view,
    unlock_user_view,
    search_audit_logs_view,
    search_database_logs_view,
    search_users_view,
    update_user_view,
    update_user_password_view,
)
from main.csvio.patient_csv_export import csv_export_list, fetch_csv_export
from main.dashboard_views import femr_admin_dashboard_view
from main.delete_views import (
    delete_chief_complaint,
    delete_treatment_view,
    patient_delete_view,
    delete_photo_view,
)
from main.femr_admin_views import lock_instance_view, unlock_instance_view
from main.formulary_management import (
    add_supply_view,
    csv_export_view,
    csv_handler_view,
    csv_import_view,
    delete_supply_item,
    edit_add_supply_view,
    edit_sub_supply_view,
    edit_supply_view,
    formulary_home_view,
)
from main.operation_admin_views import operation_admin_home_view
from main.organization_admin_views import organization_admin_home_view
from main.patient_export import patient_export_view
from main.photo_handler import edit_photo_view, upload_photo_view
from main.views import set_timezone
from .api_views import (
    UserViewSet,
    GroupViewSet,
    PatientViewSet,
    PatientEncounterViewSet,
    CampaignViewSet,
    InstanceViewSet,
    RaceViewSet,
    StateViewSet,
    EthnicityViewSet,
    MessageOfTheDayViewSet,
    UnitsSettingViewSet,
    InventoryViewSet,
    InventoryEntryViewSet,
    ManufacturerViewSet,
    InventoryFormViewSet,
    InventoryCategoryViewSet,
    TreatmentViewSet,
    PatientDiagnosisViewSet,
    VitalsViewSet,
    HistoryOfPresentIllnessViewSet,
    PhotoViewSet,
    TestViewSet,
    MedicationViewSet,
    DiagnosisViewSet,
    AdministrationScheduleViewSet,
    ChiefComplaintViewSet,
    OrganizationViewSet,
)
from .auth_views import (
    all_locked,
    not_logged_in,
    login_view,
    logout_view,
    permission_denied,
    reset_lockouts,
)
from .autocomplete_views import (
    DiagnosisAutocomplete,
    EthnicityAutocomplete,
    InventoryCategoryAutocomplete,
    InventoryEntryAutocomplete,
    InventoryFormAutocomplete,
    ManufacturerAutocomplete,
    MedicationAutocomplete,
    ChiefComplaintAutocomplete,
    AdministrationScheduleAutocomplete,
    RaceAutocomplete,
    StateAutocomplete,
    TestAutocomplete,
)
from .edit_views import (
    aux_form_view,
    history_view,
    hpi_view,
    new_diagnosis_view,
    new_treatment_view,
    patient_edit_form_view,
    encounter_edit_form_view,
    patient_medical,
    new_vitals_view,
    submit_hpi_view,
)
from .femr_admin_views import (
    edit_contact_view,
    edit_organization_view,
    list_organization_view,
    lock_campaign_view,
    new_campaign_view,
    new_contact_view,
    new_ethnicity_view,
    new_instance_view,
    edit_campaign_view,
    list_campaign_view,
    list_instance_view,
    femr_admin_home,
    change_campaign,
    new_organization_view,
    new_race_view,
    unlock_campaign_view,
    view_contact_view,
    edit_instance_view,
)
from .form_views import (
    patient_form_view,
    referral_form_view,
    patient_encounter_form_view,
)
from .list_views import (
    chief_complaint_list_view,
    patient_csv_export_view,
    patient_list_view,
    filter_patient_list_view,
    search_patient_list_view,
)
from .small_forms_views import (
    chief_complaint_form_view,
    diagnosis_form_view,
    medication_form_view,
    treatment_form_view,
)
from .views import begin_stress_test_view, forgot_username, index, home, faqs, healthcheck, help_messages_off, request_stress_test_view

# pylint: disable=C0103
app_name = "main"

schema_view = get_schema_view(
    openapi.Info(
        title="fEMR OnChain API",
        default_version="v1.6.1",
        description="API endpoints providing an interface with the fEMR OnChain application.",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="info@teamfemr.org"),
        license=openapi.License(name="GPL v3"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

router = routers.DefaultRouter()
router.register(r"Users", UserViewSet)
router.register(r"Groups", GroupViewSet)
router.register(r"Patient", PatientViewSet)
router.register(r"Encounter", PatientEncounterViewSet)
router.register(r"Campaign", CampaignViewSet)
router.register(r"Instance", InstanceViewSet)
router.register(r"Race", RaceViewSet)
router.register(r"State", StateViewSet)
router.register(r"Ethnicity", EthnicityViewSet)
router.register(r"Organization", OrganizationViewSet)
router.register(r"ChiefComplaint", ChiefComplaintViewSet)
router.register(r"AdministrationSchedule", AdministrationScheduleViewSet)
router.register(r"Diagnosis", DiagnosisViewSet)
router.register(r"Medication", MedicationViewSet)
router.register(r"Test", TestViewSet)
router.register(r"Photo", PhotoViewSet)
router.register(r"HistoryOfPresentIllness", HistoryOfPresentIllnessViewSet)
router.register(r"Vitals", VitalsViewSet)
router.register(r"PatientDiagnosis", PatientDiagnosisViewSet)
router.register(r"Treatment", TreatmentViewSet)
router.register(r"InventoryForm", InventoryFormViewSet)
router.register(r"InventoryCategory", InventoryCategoryViewSet)
router.register(r"Manufacturer", ManufacturerViewSet)
router.register(r"InventoryEntry", InventoryEntryViewSet)
router.register(r"Inventory", InventoryViewSet)
router.register(r"UnitSetting", UnitsSettingViewSet)
router.register(r"MessageOfTheDayViewSet", MessageOfTheDayViewSet)

urlpatterns = [
    re_path(r"^$", index, name="index"),
    re_path(r"^index/$", index, name="index"),
    re_path(r"^home/$", home, name="home"),
    re_path(r"^faqs/$", faqs, name="faqs"),
    re_path(r"^logout/$", logout_view, name="logout_view"),
    re_path(r"^login_view/$", login_view, name="login_view"),
    re_path(r"^not_logged_in/$", not_logged_in, name="not_logged_in"),
    re_path(r"^permission_denied/$", permission_denied, name="permission_denied"),
    re_path(r"^all_locked/$", all_locked, name="all_locked"),
    re_path(r"^healthcheck/$", healthcheck, name="healthcheck"),
    re_path(r"^patient_form_view/$", patient_form_view, name="patient_form_view"),

    path(r"request_stress_test_view/", request_stress_test_view, name="request_stress_test_view"),
    path(r"begin_stress_test_view/", begin_stress_test_view, name="begin_stress_test_view"),

    path(
        r"patient_edit_form_view/<int:patient_id>",
        patient_edit_form_view,
        name="patient_edit_form_view",
    ),
    path(
        r"patient_delete_view/<int:patient_id>",
        patient_delete_view,
        name="patient_delete_view",
    ),
    path(
        r"delete_treatment_view/<int:treatment_id>",
        delete_treatment_view,
        name="delete_treatment_view",
    ),
    path(
        r"delete_chief_complaint/<int:chief_complaint_id>/<int:patient_id>",
        delete_chief_complaint,
        name="delete_chief_complaint",
    ),
    path(
        r"delete_supply_item/<int:supply_id>",
        delete_supply_item,
        name="delete_supply_item",
    ),
    path(
        r"delete_chief_complaint/<int:chief_complaint_id>/<int:patient_id>/<int:encounter_id>",
        delete_chief_complaint,
        name="delete_chief_complaint",
    ),
    path(
        r"patient_encounter_form_view/<int:patient_id>",
        patient_encounter_form_view,
        name="patient_encounter_form_view",
    ),
    path(
        r"encounter_edit_form_view/<int:patient_id>/<int:encounter_id>",
        encounter_edit_form_view,
        name="encounter_edit_form_view",
    ),
    path(
        r"new_vitals_view/<int:patient_id>/<int:encounter_id>",
        new_vitals_view,
        name="new_vitals_view",
    ),
    path(
        r"new_diagnosis_view/<int:patient_id>/<int:encounter_id>",
        new_diagnosis_view,
        name="new_diagnosis_view",
    ),
    path(
        r"notes_view/<int:patient_id>/<int:encounter_id>",
        aux_form_view,
        name="notes_view",
    ),
    path(
        r"history_view/<int:patient_id>/<int:encounter_id>",
        history_view,
        name="history_view",
    ),
    path(
        r"new_treatment_view/<int:patient_id>/<int:encounter_id>",
        new_treatment_view,
        name="new_treatment_view",
    ),
    path(
        r"upload_photo_view/<int:patient_id>/<int:encounter_id>",
        upload_photo_view,
        name="upload_photo_view",
    ),
    path(r"hpi_view/<int:patient_id>/<int:encounter_id>", hpi_view, name="hpi_view"),
    path(
        r"submit_hpi_view/<int:patient_id>/<int:encounter_id>/<int:hpi_id>",
        submit_hpi_view,
        name="submit_hpi_view",
    ),
    path(
        r"edit_photo_view/<int:patient_id>/<int:encounter_id>/<int:photo_id>",
        edit_photo_view,
        name="edit_photo_view",
    ),
    path(
        r"delete_photo_view/<int:patient_id>/<int:encounter_id>/<int:photo_id>",
        delete_photo_view,
        name="delete_photo_view",
    ),
    path(r"patient_medical/<int:patient_id>", patient_medical, name="patient_medical"),
    path(
        r"referral_form/<int:patient_id>", referral_form_view, name="referral_form_view"
    ),
    re_path(r"^patient_list_view/$", patient_list_view, name="patient_list_view"),
    path(
        r"chief_complaint_list_view/<int:patient_id>/<int:encounter_id>",
        chief_complaint_list_view,
        name="chief_complaint_list_view",
    ),
    path(
        r"chief_complaint_list_view/<int:patient_id>",
        chief_complaint_list_view,
        name="chief_complaint_list_view",
    ),
    path(
        r"patient_csv_export_view/<int:timeframe>",
        patient_csv_export_view,
        name="patient_csv_export_view",
    ),
    re_path(
        r"^search_patient_list_view/$",
        search_patient_list_view,
        name="search_patient_list_view",
    ),
    re_path(
        r"^filter_patient_list_view/$",
        filter_patient_list_view,
        name="filter_patient_list_view",
    ),
    re_path(r"^superuser_home/$", admin_home, name="superuser_home"),
    re_path(r"^set_timezone/$", set_timezone, name="set_timezone"),
    re_path(
        r"^message_of_the_day_view/$",
        message_of_the_day_view,
        name="message_of_the_day_view",
    ),
    # User Management
    re_path(r"^list_users_view/$", list_users_view, name="list_users_view"),
    re_path(r"^create_user_view/$", create_user_view, name="create_user_view"),
    path(r"update_user_view/<int:user_id>", update_user_view, name="update_user_view"),
    path(
        r"update_user_password_view/<int:user_id>",
        update_user_password_view,
        name="update_user_password_view",
    ),
    path(r"lock_users_view/<int:user_id>", lock_user_view, name="lock_user_view"),
    path(r"unlock_users_view/<int:user_id>", unlock_user_view, name="unlock_user_view"),
    re_path(r"^filter_users_view/$", filter_users_view, name="filter_user_view"),
    re_path(r"^search_users_view/$", search_users_view, name="search_user_view"),
    path(
        r"lock_instance_view/<int:instance_id>",
        lock_instance_view,
        name="lock_instance_view",
    ),
    path(
        r"unlock_instance_view/<int:instance_id>",
        unlock_instance_view,
        name="unlock_instance_view",
    ),
    path(
        r"lock_campaign_view/<int:campaign_id>",
        lock_campaign_view,
        name="lock_campaign_view",
    ),
    path(
        r"unlock_campaign_view/<int:campaign_id>",
        unlock_campaign_view,
        name="unlock_campaign_view",
    ),
    path(r"reset_lockouts", reset_lockouts, name="reset_lockouts"),
    path(r"reset_lockouts/<str:username>", reset_lockouts, name="reset_lockouts"),
    # Audit Log Management
    re_path(r"^get_audit_logs_view/$", get_audit_logs_view, name="get_audit_logs_view"),
    re_path(
        r"^export_audit_logs_view/$",
        export_audit_logs_view,
        name="export_audit_logs_view",
    ),
    re_path(
        r"^filter_audit_logs_view/$",
        filter_audit_logs_view,
        name="filter_audit_logs_view",
    ),
    re_path(
        r"^search_audit_logs_view/$",
        search_audit_logs_view,
        name="search_audit_logs_view",
    ),
    # Database Log Management
    re_path(
        r"^get_database_logs_view/$",
        get_database_logs_view,
        name="get_database_logs_view",
    ),
    re_path(
        r"^export_database_logs_view/$",
        export_database_logs_view,
        name="export_database_logs_view",
    ),
    re_path(
        r"^search_database_logs_view/$",
        search_database_logs_view,
        name="search_database_logs_view",
    ),
    re_path(
        r"^filter_database_logs_view/$",
        filter_database_logs_view,
        name="filter_database_logs_view",
    ),
    # Formulary Management
    re_path(r"^formulary_home_view/$", formulary_home_view, name="formulary_home_view"),
    re_path(r"^add_supply_view/$", add_supply_view, name="add_supply_view"),
    path(r"edit_supply/<int:entry_id>", edit_supply_view, name="edit_supply_view"),
    path(
        r"edit_add_supply_view/<int:entry_id>",
        edit_add_supply_view,
        name="edit_add_supply_view",
    ),
    path(
        r"edit_sub_supply_view/<int:entry_id>",
        edit_sub_supply_view,
        name="edit_sub_supply_view",
    ),
    re_path(r"^csv_handler_view/$", csv_handler_view, name="csv_handler_view"),
    re_path(r"^csv_import_view/$", csv_import_view, name="csv_import_view"),
    re_path(r"^csv_export_view/$", csv_export_view, name="csv_export_view"),
    re_path(r"^csv_export_list/$", csv_export_list, name="csv_export_list"),
    path(
        r"fetch_csv_export/<int:export_id>", fetch_csv_export, name="fetch_csv_export"
    ),
    # fEMR Environment Management
    re_path(r"^femr_admin_home/$", femr_admin_home, name="femr_admin_home"),
    re_path(r"^change_campaign/$", change_campaign, name="change_campaign"),
    re_path(r"^list_campaign/$", list_campaign_view, name="list_campaign"),
    path(r"edit_campaign/<int:campaign_id>", edit_campaign_view, name="edit_campaign"),
    re_path(r"^new_campaign/$", new_campaign_view, name="new_campaign"),
    re_path(r"^list_instance/$", list_instance_view, name="list_instance"),
    path(r"edit_instance/<int:instance_id>", edit_instance_view, name="edit_instance"),
    re_path(r"^new_instance/$", new_instance_view, name="new_instance"),
    path(r"edit_contact/<int:contact_id>", edit_contact_view, name="edit_contact"),
    path(r"view_contact/<int:contact_id>", view_contact_view, name="view_contact"),
    re_path(r"^new_contact/$", new_contact_view, name="new_contact"),
    path(
        r"patient_export/<int:patient_id>", patient_export_view, name="patient_export"
    ),
    re_path(r"^new_race/$", new_race_view, name="new_race"),
    re_path(r"^new_ethnicity/$", new_ethnicity_view, name="new_ethnicity"),
    re_path(r"^list_organization/$", list_organization_view, name="list_organization"),
    re_path(r"^new_organization/$", new_organization_view, name="new_organization"),
    path(
        r"edit_organization/<int:organization_id>",
        edit_organization_view,
        name="edit_organization",
    ),
    # Operation Management
    path(
        r"organization_admin_home_view/",
        organization_admin_home_view,
        name="organization_admin_home_view",
    ),
    # Organization Management
    path(
        r"operation_admin_home_view/",
        operation_admin_home_view,
        name="operation_admin_home_view",
    ),
    path(
        r"chief_complaint_form_view",
        chief_complaint_form_view,
        name="chief_complaint_form_view",
    ),
    path(r"diagnosis_form_view", diagnosis_form_view, name="diagnosis_form_view"),
    path(r"medication_form_view", medication_form_view, name="medication_form_view"),
    path(r"treatment_form_view", treatment_form_view, name="treatment_form_view"),
    path(r"add_users_to_campaign", add_users_to_campaign, name="add_users_to_campaign"),
    path(
        r"add_user_to_campaign/<int:user_id>",
        add_user_to_campaign,
        name="add_user_to_campaign",
    ),
    path(
        r"cut_user_from_campaign/<int:user_id>",
        cut_user_from_campaign,
        name="cut_user_from_campaign",
    ),
    path("api/", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    re_path(
        r"^get_auth_token/$",
        rest_framework_views.obtain_auth_token,
        name="get_auth_token",
    ),
    re_path(
        r"^swagger(?P<format>\.json|\.yaml)$",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    re_path(
        r"^swagger/$",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    re_path(
        r"^redoc/$", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"
    ),
    re_path(r"^forgot_username", forgot_username, name="forgot_username"),
    re_path(r"^help_messages_off", help_messages_off, name="help_messages_off"),
    re_path(
        r"^femr_admin_dashboard_view",
        femr_admin_dashboard_view,
        name="femr_admin_dashboard_view",
    ),
    re_path(
        r"^diagnosis-autocomplete/$",
        DiagnosisAutocomplete.as_view(create_field="text"),
        name="diagnosis-autocomplete",
    ),
    re_path(
        r"^medication-autocomplete/$",
        MedicationAutocomplete.as_view(create_field="text"),
        name="medication-autocomplete",
    ),
    re_path(
        r"^inventory-entry-autocomplete/$",
        InventoryEntryAutocomplete.as_view(),
        name="inventory-entry-autocomplete",
    ),
    re_path(
        r"^inventory-form-autocomplete/$",
        InventoryFormAutocomplete.as_view(create_field="name"),
        name="inventory-form-autocomplete",
    ),
    re_path(
        r"^inventory-category-autocomplete/$",
        InventoryCategoryAutocomplete.as_view(create_field="name"),
        name="inventory-category-autocomplete",
    ),
    re_path(
        r"^manufacturer-autocomplete/$",
        ManufacturerAutocomplete.as_view(create_field="name"),
        name="manufacturer-autocomplete",
    ),
    re_path(
        r"^test-autocomplete/$",
        TestAutocomplete.as_view(create_field="text"),
        name="test-autocomplete",
    ),
    re_path(
        r"^chief-complaint-autocomplete/$",
        ChiefComplaintAutocomplete.as_view(create_field="text"),
        name="chief-complaint-autocomplete",
    ),
    re_path(
        r"^administration-schedule-autocomplete/$",
        AdministrationScheduleAutocomplete.as_view(create_field="text"),
        name="administration-schedule-autocomplete",
    ),
    re_path(
        r"^race-autocomplete/$",
        RaceAutocomplete.as_view(create_field="name"),
        name="race-autocomplete",
    ),
    re_path(
        r"^ethnicity-autocomplete/$",
        EthnicityAutocomplete.as_view(create_field="name"),
        name="ethnicity-autocomplete",
    ),
    re_path(
        r"^state-autocomplete/$",
        StateAutocomplete.as_view(create_field="name"),
        name="state-autocomplete",
    ),
]
