# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.contrib.gis.db import models


class AduPermits(models.Model):
    ivr_number = models.BigIntegerField(
        db_column="IVR_NUMBER", blank=True, null=True
    )  # Field name made lowercase.
    application_number = models.TextField(
        db_column="APPLICATION_NUMBER", blank=True, null=True
    )  # Field name made lowercase.
    status = models.TextField(
        db_column="STATUS", blank=True, null=True
    )  # Field name made lowercase.
    type = models.TextField(
        db_column="TYPE", blank=True, null=True
    )  # Field name made lowercase.
    description = models.TextField(
        db_column="DESCRIPTION", blank=True, null=True
    )  # Field name made lowercase.
    work = models.TextField(
        db_column="WORK", blank=True, null=True
    )  # Field name made lowercase.
    address = models.TextField(
        db_column="ADDRESS", blank=True, null=True
    )  # Field name made lowercase.
    state_id = models.TextField(
        db_column="STATE_ID", blank=True, null=True
    )  # Field name made lowercase.
    property_id = models.TextField(
        db_column="PROPERTY_ID", blank=True, null=True
    )  # Field name made lowercase.
    set_up = models.TextField(
        db_column="SET_UP", blank=True, null=True
    )  # Field name made lowercase.
    under_review = models.TextField(
        db_column="UNDER_REVIEW", blank=True, null=True
    )  # Field name made lowercase.
    issued = models.TextField(
        db_column="ISSUED", blank=True, null=True
    )  # Field name made lowercase.
    final = models.TextField(
        db_column="FINAL", blank=True, null=True
    )  # Field name made lowercase.
    neighborhood = models.TextField(
        db_column="NEIGHBORHOOD", blank=True, null=True
    )  # Field name made lowercase.
    neighborhood_coalition = models.TextField(
        db_column="NEIGHBORHOOD_COALITION", blank=True, null=True
    )  # Field name made lowercase.
    business_association = models.TextField(
        db_column="BUSINESS_ASSOCIATION", blank=True, null=True
    )  # Field name made lowercase.
    county = models.TextField(
        db_column="COUNTY", blank=True, null=True
    )  # Field name made lowercase.
    x_web_mercator = models.FloatField(
        db_column="X_WEB_MERCATOR", blank=True, null=True
    )  # Field name made lowercase.
    y_web_mercator = models.FloatField(
        db_column="Y_WEB_MERCATOR", blank=True, null=True
    )  # Field name made lowercase.
    ccb_number = models.TextField(
        db_column="CCB_NUMBER", blank=True, null=True
    )  # Field name made lowercase.
    occupancy_group = models.TextField(
        db_column="OCCUPANCY_GROUP", blank=True, null=True
    )  # Field name made lowercase.
    construction_type = models.TextField(
        db_column="CONSTRUCTION_TYPE", blank=True, null=True
    )  # Field name made lowercase.
    submitted_valuation = models.FloatField(
        db_column="SUBMITTED_VALUATION", blank=True, null=True
    )  # Field name made lowercase.
    final_valuation = models.FloatField(
        db_column="FINAL_VALUATION", blank=True, null=True
    )  # Field name made lowercase.
    new_units = models.FloatField(
        db_column="NEW_UNITS", blank=True, null=True
    )  # Field name made lowercase.
    total_sqft = models.FloatField(
        db_column="TOTAL_SQFT", blank=True, null=True
    )  # Field name made lowercase.
    stories = models.FloatField(
        db_column="STORIES", blank=True, null=True
    )  # Field name made lowercase.
    customer = models.FloatField(
        db_column="CUSTOMER", blank=True, null=True
    )  # Field name made lowercase.
    geometry = models.PointField(srid=3857, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "adu_permits"


class BgRents(models.Model):
    geoid = models.TextField(
        db_column="GEOID", blank=True, null=True
    )  # Field name made lowercase.
    one_bed_rent_sf = models.FloatField(blank=True, null=True)
    two_bed_rent_sf = models.FloatField(blank=True, null=True)
    geometry = models.PolygonField(srid=4269, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "bg_rents"


class Buildings(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    bldg_id = models.TextField(
        db_column="BLDG_ID", blank=True, null=True
    )  # Field name made lowercase.
    state_id = models.TextField(
        db_column="STATE_ID", blank=True, null=True
    )  # Field name made lowercase.
    bldg_numb = models.BigIntegerField(
        db_column="BLDG_NUMB", blank=True, null=True
    )  # Field name made lowercase.
    bldg_name = models.TextField(
        db_column="BLDG_NAME", blank=True, null=True
    )  # Field name made lowercase.
    bldg_addr = models.TextField(
        db_column="BLDG_ADDR", blank=True, null=True
    )  # Field name made lowercase.
    bldg_type = models.TextField(
        db_column="BLDG_TYPE", blank=True, null=True
    )  # Field name made lowercase.
    bldg_use = models.TextField(
        db_column="BLDG_USE", blank=True, null=True
    )  # Field name made lowercase.
    bldg_sqft = models.FloatField(
        db_column="BLDG_SQFT", blank=True, null=True
    )  # Field name made lowercase.
    sqft_src = models.TextField(
        db_column="SQFT_SRC", blank=True, null=True
    )  # Field name made lowercase.
    sqft_conf = models.TextField(
        db_column="SQFT_CONF", blank=True, null=True
    )  # Field name made lowercase.
    num_story = models.FloatField(
        db_column="NUM_STORY", blank=True, null=True
    )  # Field name made lowercase.
    num_units = models.FloatField(
        db_column="NUM_UNITS", blank=True, null=True
    )  # Field name made lowercase.
    year_built = models.FloatField(
        db_column="YEAR_BUILT", blank=True, null=True
    )  # Field name made lowercase.
    ecoroof = models.TextField(
        db_column="ECOROOF", blank=True, null=True
    )  # Field name made lowercase.
    leed_rate = models.TextField(
        db_column="LEED_RATE", blank=True, null=True
    )  # Field name made lowercase.
    source = models.TextField(
        db_column="SOURCE", blank=True, null=True
    )  # Field name made lowercase.
    source_ref = models.TextField(
        db_column="SOURCE_REF", blank=True, null=True
    )  # Field name made lowercase.
    avg_height = models.FloatField(
        db_column="AVG_HEIGHT", blank=True, null=True
    )  # Field name made lowercase.
    max_height = models.FloatField(
        db_column="MAX_HEIGHT", blank=True, null=True
    )  # Field name made lowercase.
    min_height = models.FloatField(
        db_column="MIN_HEIGHT", blank=True, null=True
    )  # Field name made lowercase.
    height_src = models.TextField(
        db_column="HEIGHT_SRC", blank=True, null=True
    )  # Field name made lowercase.
    heightconf = models.TextField(
        db_column="HEIGHTCONF", blank=True, null=True
    )  # Field name made lowercase.
    surf_elev = models.FloatField(
        db_column="SURF_ELEV", blank=True, null=True
    )  # Field name made lowercase.
    surf_off = models.FloatField(
        db_column="SURF_OFF", blank=True, null=True
    )  # Field name made lowercase.
    surf_adj = models.FloatField(
        db_column="SURF_ADJ", blank=True, null=True
    )  # Field name made lowercase.
    surf_src = models.TextField(
        db_column="SURF_SRC", blank=True, null=True
    )  # Field name made lowercase.
    roof_elev = models.FloatField(
        db_column="ROOF_ELEV", blank=True, null=True
    )  # Field name made lowercase.
    roof_type = models.TextField(
        db_column="ROOF_TYPE", blank=True, null=True
    )  # Field name made lowercase.
    orient = models.FloatField(
        db_column="ORIENT", blank=True, null=True
    )  # Field name made lowercase.
    volume = models.FloatField(
        db_column="VOLUME", blank=True, null=True
    )  # Field name made lowercase.
    multi_poly = models.TextField(
        db_column="MULTI_POLY", blank=True, null=True
    )  # Field name made lowercase.
    modifier = models.TextField(
        db_column="MODIFIER", blank=True, null=True
    )  # Field name made lowercase.
    mod_name = models.TextField(
        db_column="MOD_NAME", blank=True, null=True
    )  # Field name made lowercase.
    mod_date = models.TextField(
        db_column="MOD_DATE", blank=True, null=True
    )  # Field name made lowercase.
    created_by = models.TextField(
        db_column="CREATED_BY", blank=True, null=True
    )  # Field name made lowercase.
    createdate = models.TextField(
        db_column="CREATEDATE", blank=True, null=True
    )  # Field name made lowercase.
    field_date = models.TextField(
        db_column="FIELD_DATE", blank=True, null=True
    )  # Field name made lowercase.
    review = models.TextField(
        db_column="REVIEW", blank=True, null=True
    )  # Field name made lowercase.
    notes = models.TextField(
        db_column="NOTES", blank=True, null=True
    )  # Field name made lowercase.
    subarea = models.TextField(
        db_column="SUBAREA", blank=True, null=True
    )  # Field name made lowercase.
    lat_ctr = models.FloatField(
        db_column="LAT_CTR", blank=True, null=True
    )  # Field name made lowercase.
    long_ctr = models.FloatField(
        db_column="LONG_CTR", blank=True, null=True
    )  # Field name made lowercase.
    usgs_quad = models.TextField(
        db_column="USGS_QUAD", blank=True, null=True
    )  # Field name made lowercase.
    wsuniqueid = models.TextField(
        db_column="WSUNIQUEID", blank=True, null=True
    )  # Field name made lowercase.
    bps_bldgid = models.FloatField(
        db_column="BPS_BLDGID", blank=True, null=True
    )  # Field name made lowercase.
    area = models.FloatField(
        db_column="AREA", blank=True, null=True
    )  # Field name made lowercase.
    length = models.FloatField(
        db_column="LENGTH", blank=True, null=True
    )  # Field name made lowercase.
    geometry = models.GeometryField(srid=2913, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "buildings"


class CostarMultifamilyRent(models.Model):
    property_address = models.TextField(blank=True, null=True)
    property_name = models.TextField(blank=True, null=True)
    star_rating = models.BigIntegerField(blank=True, null=True)
    energy_star = models.TextField(blank=True, null=True)
    leed_certified = models.TextField(blank=True, null=True)
    building_status = models.TextField(blank=True, null=True)
    rba = models.FloatField(blank=True, null=True)
    secondary_type = models.TextField(blank=True, null=True)
    market_name = models.TextField(blank=True, null=True)
    submarket_name = models.TextField(blank=True, null=True)
    city = models.TextField(blank=True, null=True)
    state = models.TextField(blank=True, null=True)
    zip = models.TextField(blank=True, null=True)
    county_name = models.TextField(blank=True, null=True)
    for_sale_price = models.FloatField(blank=True, null=True)
    for_sale_status = models.TextField(blank=True, null=True)
    year_built = models.BigIntegerField(blank=True, null=True)
    year_renovated = models.FloatField(blank=True, null=True)
    building_park = models.TextField(blank=True, null=True)
    zoning = models.TextField(blank=True, null=True)
    number_of_units = models.BigIntegerField(blank=True, null=True)
    style = models.TextField(blank=True, null=True)
    total_buildings = models.FloatField(blank=True, null=True)
    number_of_stories = models.FloatField(blank=True, null=True)
    price_unit = models.FloatField(blank=True, null=True)
    cap_rate = models.FloatField(blank=True, null=True)
    vacancy_pct = models.FloatField(blank=True, null=True)
    avg_unit_sf = models.FloatField(blank=True, null=True)
    avg_asking_unit = models.FloatField(blank=True, null=True)
    avg_asking_sf = models.FloatField(blank=True, null=True)
    avg_effective_unit = models.FloatField(blank=True, null=True)
    avg_effective_sf = models.FloatField(blank=True, null=True)
    avg_concessions_pct = models.FloatField(blank=True, null=True)
    pct_studios = models.FloatField(blank=True, null=True)
    pct_1_bed = models.FloatField(blank=True, null=True)
    pct_2_bed = models.FloatField(blank=True, null=True)
    pct_3_bed = models.FloatField(blank=True, null=True)
    pct_4_bed = models.FloatField(blank=True, null=True)
    rent_type = models.TextField(blank=True, null=True)
    affordable_type = models.TextField(blank=True, null=True)
    market_segment = models.TextField(blank=True, null=True)
    parking_spaces_unit = models.FloatField(blank=True, null=True)
    number_of_parking_spaces = models.FloatField(blank=True, null=True)
    days_on_market = models.FloatField(blank=True, null=True)
    amenities = models.TextField(blank=True, null=True)
    anchor_gla = models.FloatField(blank=True, null=True)
    anchor_tenants = models.TextField(blank=True, null=True)
    architect_name = models.TextField(blank=True, null=True)
    average_weighted_rent = models.TextField(blank=True, null=True)
    avg_asking_bed = models.FloatField(blank=True, null=True)
    avg_rent_direct_industrial = models.FloatField(blank=True, null=True)
    avg_rent_direct_office = models.FloatField(blank=True, null=True)
    avg_rent_direct_retail = models.FloatField(blank=True, null=True)
    avg_rent_sublet_industrial = models.FloatField(blank=True, null=True)
    avg_rent_sublet_office = models.FloatField(blank=True, null=True)
    avg_rent_sublet_retail = models.FloatField(blank=True, null=True)
    building_class = models.TextField(blank=True, null=True)
    building_operating_expenses = models.TextField(blank=True, null=True)
    building_tax_expenses = models.TextField(blank=True, null=True)
    ceiling_height_range = models.FloatField(blank=True, null=True)
    closest_transit_stop = models.TextField(blank=True, null=True)
    closest_transit_stop_dist_mi = models.FloatField(blank=True, null=True)
    closest_transit_stop_walk_time_min = models.FloatField(blank=True, null=True)
    column_spacing = models.FloatField(blank=True, null=True)
    construction_material = models.TextField(blank=True, null=True)
    core_factor = models.FloatField(blank=True, null=True)
    cross_street = models.TextField(blank=True, null=True)
    developer_name = models.TextField(blank=True, null=True)
    direct_available_space = models.FloatField(blank=True, null=True)
    direct_services = models.TextField(blank=True, null=True)
    direct_vacant_space = models.BigIntegerField(blank=True, null=True)
    drive_ins = models.TextField(blank=True, null=True)
    exp_year = models.FloatField(blank=True, null=True)
    features = models.TextField(blank=True, null=True)
    four_bedroom_asking_rent_bed = models.FloatField(blank=True, null=True)
    four_bedroom_asking_rent_sf = models.FloatField(blank=True, null=True)
    four_bedroom_asking_rent_unit = models.FloatField(blank=True, null=True)
    four_bedroom_avg_sf = models.FloatField(blank=True, null=True)
    four_bedroom_concessions_pct = models.FloatField(blank=True, null=True)
    four_bedroom_effective_rent_bed = models.FloatField(blank=True, null=True)
    four_bedroom_effective_rent_sf = models.FloatField(blank=True, null=True)
    four_bedroom_effective_rent_unit = models.FloatField(blank=True, null=True)
    four_bedroom_vacancy_pct = models.FloatField(blank=True, null=True)
    four_bedroom_vacant_units = models.FloatField(blank=True, null=True)
    gas = models.FloatField(blank=True, null=True)
    heating = models.FloatField(blank=True, null=True)
    land_area_ac = models.FloatField(blank=True, null=True)
    land_area_sf = models.FloatField(blank=True, null=True)
    last_sale_date = models.DateTimeField(blank=True, null=True)
    last_sale_price = models.FloatField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    leasing_company_address = models.TextField(blank=True, null=True)
    leasing_company_city_state_zip = models.TextField(blank=True, null=True)
    leasing_company_contact = models.TextField(blank=True, null=True)
    leasing_company_fax = models.FloatField(blank=True, null=True)
    leasing_company_name = models.TextField(blank=True, null=True)
    leasing_company_phone = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    max_building_contiguous_space = models.FloatField(blank=True, null=True)
    max_floor_contiguous_space = models.FloatField(blank=True, null=True)
    number_of_1_bedrooms_units = models.FloatField(blank=True, null=True)
    number_of_2_bedrooms_units = models.FloatField(blank=True, null=True)
    number_of_3_bedrooms_units = models.FloatField(blank=True, null=True)
    number_of_4_bedrooms_units = models.FloatField(blank=True, null=True)
    number_of_beds = models.FloatField(blank=True, null=True)
    number_of_cranes = models.FloatField(blank=True, null=True)
    number_of_elevators = models.BigIntegerField(blank=True, null=True)
    number_of_loading_docks = models.FloatField(blank=True, null=True)
    number_of_rooms = models.FloatField(blank=True, null=True)
    number_of_studios_units = models.FloatField(blank=True, null=True)
    office_space = models.FloatField(blank=True, null=True)
    one_bedroom_asking_rent_bed = models.FloatField(blank=True, null=True)
    one_bedroom_asking_rent_sf = models.FloatField(blank=True, null=True)
    one_bedroom_asking_rent_unit = models.FloatField(blank=True, null=True)
    one_bedroom_avg_sf = models.FloatField(blank=True, null=True)
    one_bedroom_concessions_pct = models.FloatField(blank=True, null=True)
    one_bedroom_effective_rent_bed = models.FloatField(blank=True, null=True)
    one_bedroom_effective_rent_sf = models.FloatField(blank=True, null=True)
    one_bedroom_effective_rent_unit = models.FloatField(blank=True, null=True)
    one_bedroom_vacancy_pct = models.FloatField(blank=True, null=True)
    one_bedroom_vacant_units = models.FloatField(blank=True, null=True)
    ops_expense = models.FloatField(blank=True, null=True)
    ops_expense_per_sf = models.FloatField(blank=True, null=True)
    owner_address = models.TextField(blank=True, null=True)
    owner_city_state_zip = models.TextField(blank=True, null=True)
    owner_contact = models.TextField(blank=True, null=True)
    owner_name = models.TextField(blank=True, null=True)
    owner_phone = models.FloatField(blank=True, null=True)
    parcel_number_1min = models.TextField(blank=True, null=True)
    parcel_number_2max = models.TextField(blank=True, null=True)
    parking_ratio = models.FloatField(blank=True, null=True)
    percent_leased = models.FloatField(blank=True, null=True)
    power = models.FloatField(blank=True, null=True)
    pre_leasing = models.FloatField(blank=True, null=True)
    primary_agent_name = models.TextField(blank=True, null=True)
    property_location = models.TextField(blank=True, null=True)
    property_manager_address = models.TextField(blank=True, null=True)
    property_manager_city_state_zip = models.TextField(blank=True, null=True)
    property_manager_contact = models.TextField(blank=True, null=True)
    property_manager_name = models.TextField(blank=True, null=True)
    property_manager_phone = models.FloatField(blank=True, null=True)
    propertyid = models.BigIntegerField(blank=True, null=True)
    propertytype = models.TextField(blank=True, null=True)
    proposed_land_use = models.FloatField(blank=True, null=True)
    rail_lines = models.FloatField(blank=True, null=True)
    recorded_owner_address = models.TextField(blank=True, null=True)
    recorded_owner_city_state_zip = models.TextField(blank=True, null=True)
    recorded_owner_contact = models.TextField(blank=True, null=True)
    recorded_owner_name = models.TextField(blank=True, null=True)
    recorded_owner_phone = models.FloatField(blank=True, null=True)
    rent_sf_yr = models.TextField(blank=True, null=True)
    sale_company_address = models.TextField(blank=True, null=True)
    sale_company_city_state_zip = models.TextField(blank=True, null=True)
    sale_company_contact = models.TextField(blank=True, null=True)
    sale_company_fax = models.FloatField(blank=True, null=True)
    sale_company_name = models.TextField(blank=True, null=True)
    sale_company_phone = models.FloatField(blank=True, null=True)
    sales_company = models.TextField(blank=True, null=True)
    sales_contact = models.TextField(blank=True, null=True)
    sales_contact_phone = models.FloatField(blank=True, null=True)
    services = models.TextField(blank=True, null=True)
    sewer = models.TextField(blank=True, null=True)
    smallest_available_space = models.FloatField(blank=True, null=True)
    sprinklers = models.TextField(blank=True, null=True)
    studio_asking_rent_bed = models.FloatField(blank=True, null=True)
    studio_asking_rent_sf = models.FloatField(blank=True, null=True)
    studio_asking_rent_unit = models.FloatField(blank=True, null=True)
    studio_avg_sf = models.FloatField(blank=True, null=True)
    studio_concessions_pct = models.FloatField(blank=True, null=True)
    studio_effective_rent_bed = models.FloatField(blank=True, null=True)
    studio_effective_rent_sf = models.FloatField(blank=True, null=True)
    studio_effective_rent_unit = models.FloatField(blank=True, null=True)
    studio_vacancy_pct = models.FloatField(blank=True, null=True)
    studio_vacant_units = models.FloatField(blank=True, null=True)
    sublet_available_space = models.FloatField(blank=True, null=True)
    sublet_services = models.FloatField(blank=True, null=True)
    sublet_vacant_space = models.BigIntegerField(blank=True, null=True)
    submarket_cluster = models.TextField(blank=True, null=True)
    tax_year = models.FloatField(blank=True, null=True)
    taxes_per_sf = models.FloatField(blank=True, null=True)
    taxes_total = models.FloatField(blank=True, null=True)
    tenancy = models.TextField(blank=True, null=True)
    three_bedroom_asking_rent_bed = models.FloatField(blank=True, null=True)
    three_bedroom_asking_rent_sf = models.FloatField(blank=True, null=True)
    three_bedroom_asking_rent_unit = models.FloatField(blank=True, null=True)
    three_bedroom_avg_sf = models.FloatField(blank=True, null=True)
    three_bedroom_concessions_pct = models.FloatField(blank=True, null=True)
    three_bedroom_effective_rent_bed = models.FloatField(blank=True, null=True)
    three_bedroom_effective_rent_sf = models.FloatField(blank=True, null=True)
    three_bedroom_effective_rent_unit = models.FloatField(blank=True, null=True)
    three_bedroom_vacancy_pct = models.FloatField(blank=True, null=True)
    three_bedroom_vacant_units = models.FloatField(blank=True, null=True)
    total_available_space_sf = models.FloatField(blank=True, null=True)
    total_new_space_sf = models.FloatField(blank=True, null=True)
    total_relet_space_sf = models.FloatField(blank=True, null=True)
    total_sublet_space_sf = models.FloatField(blank=True, null=True)
    total_vacant_avail_relet_space_sf = models.FloatField(blank=True, null=True)
    total_vacant_avail_sublet_space_sf = models.FloatField(blank=True, null=True)
    total_vacant_available = models.FloatField(blank=True, null=True)
    true_owner_address = models.TextField(blank=True, null=True)
    true_owner_city_state_zip = models.TextField(blank=True, null=True)
    true_owner_contact = models.TextField(blank=True, null=True)
    true_owner_name = models.TextField(blank=True, null=True)
    true_owner_phone = models.FloatField(blank=True, null=True)
    two_bedroom_asking_rent_bed = models.FloatField(blank=True, null=True)
    two_bedroom_asking_rent_sf = models.FloatField(blank=True, null=True)
    two_bedroom_asking_rent_unit = models.FloatField(blank=True, null=True)
    two_bedroom_avg_sf = models.FloatField(blank=True, null=True)
    two_bedroom_concessions_pct = models.FloatField(blank=True, null=True)
    two_bedroom_effective_rent_bed = models.FloatField(blank=True, null=True)
    two_bedroom_effective_rent_sf = models.FloatField(blank=True, null=True)
    two_bedroom_effective_rent_unit = models.FloatField(blank=True, null=True)
    two_bedroom_vacancy_pct = models.FloatField(blank=True, null=True)
    two_bedroom_vacant_units = models.FloatField(blank=True, null=True)
    typical_floor_size = models.FloatField(blank=True, null=True)
    university = models.TextField(blank=True, null=True)
    water = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "costar_multifamily_rent"


class Fwy(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    prefix = models.TextField(
        db_column="PREFIX", blank=True, null=True
    )  # Field name made lowercase.
    streetname = models.TextField(
        db_column="STREETNAME", blank=True, null=True
    )  # Field name made lowercase.
    ftype = models.TextField(
        db_column="FTYPE", blank=True, null=True
    )  # Field name made lowercase.
    type = models.BigIntegerField(
        db_column="TYPE", blank=True, null=True
    )  # Field name made lowercase.
    length = models.FloatField(
        db_column="LENGTH", blank=True, null=True
    )  # Field name made lowercase.
    geometry = models.LineStringField(srid=2913, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "fwy"


class JoinedAduPermitsToTaxlots(models.Model):
    tlid = models.TextField(
        db_column="TLID", blank=True, null=True
    )  # Field name made lowercase.
    primaccnum = models.TextField(
        db_column="PRIMACCNUM", blank=True, null=True
    )  # Field name made lowercase.
    altaccnum = models.TextField(
        db_column="ALTACCNUM", blank=True, null=True
    )  # Field name made lowercase.
    siteaddr = models.TextField(
        db_column="SITEADDR", blank=True, null=True
    )  # Field name made lowercase.
    sitecity = models.TextField(
        db_column="SITECITY", blank=True, null=True
    )  # Field name made lowercase.
    sitezip = models.TextField(
        db_column="SITEZIP", blank=True, null=True
    )  # Field name made lowercase.
    landval = models.BigIntegerField(
        db_column="LANDVAL", blank=True, null=True
    )  # Field name made lowercase.
    bldgval = models.BigIntegerField(
        db_column="BLDGVAL", blank=True, null=True
    )  # Field name made lowercase.
    totalval = models.BigIntegerField(
        db_column="TOTALVAL", blank=True, null=True
    )  # Field name made lowercase.
    bldgsqft = models.FloatField(
        db_column="BLDGSQFT", blank=True, null=True
    )  # Field name made lowercase.
    a_t_acres = models.FloatField(
        db_column="A_T_ACRES", blank=True, null=True
    )  # Field name made lowercase.
    yearbuilt = models.BigIntegerField(
        db_column="YEARBUILT", blank=True, null=True
    )  # Field name made lowercase.
    landuse = models.TextField(
        db_column="LANDUSE", blank=True, null=True
    )  # Field name made lowercase.
    saledate = models.TextField(
        db_column="SALEDATE", blank=True, null=True
    )  # Field name made lowercase.
    saleprice = models.BigIntegerField(
        db_column="SALEPRICE", blank=True, null=True
    )  # Field name made lowercase.
    county_x = models.TextField(
        db_column="COUNTY_x", blank=True, null=True
    )  # Field name made lowercase.
    x_coord = models.BigIntegerField(
        db_column="X_COORD", blank=True, null=True
    )  # Field name made lowercase.
    y_coord = models.BigIntegerField(
        db_column="Y_COORD", blank=True, null=True
    )  # Field name made lowercase.
    gis_acres = models.FloatField(
        db_column="GIS_ACRES", blank=True, null=True
    )  # Field name made lowercase.
    ortaxlot = models.TextField(
        db_column="ORTAXLOT", blank=True, null=True
    )  # Field name made lowercase.
    geometry = models.PolygonField(srid=3857, blank=True, null=True)
    ivr_number = models.BigIntegerField(
        db_column="IVR_NUMBER", blank=True, null=True
    )  # Field name made lowercase.
    application_number = models.TextField(
        db_column="APPLICATION_NUMBER", blank=True, null=True
    )  # Field name made lowercase.
    status = models.TextField(
        db_column="STATUS", blank=True, null=True
    )  # Field name made lowercase.
    type = models.TextField(
        db_column="TYPE", blank=True, null=True
    )  # Field name made lowercase.
    description = models.TextField(
        db_column="DESCRIPTION", blank=True, null=True
    )  # Field name made lowercase.
    work = models.TextField(
        db_column="WORK", blank=True, null=True
    )  # Field name made lowercase.
    address = models.TextField(
        db_column="ADDRESS", blank=True, null=True
    )  # Field name made lowercase.
    state_id = models.TextField(
        db_column="STATE_ID", blank=True, null=True
    )  # Field name made lowercase.
    property_id = models.TextField(
        db_column="PROPERTY_ID", blank=True, null=True
    )  # Field name made lowercase.
    set_up = models.TextField(
        db_column="SET_UP", blank=True, null=True
    )  # Field name made lowercase.
    under_review = models.TextField(
        db_column="UNDER_REVIEW", blank=True, null=True
    )  # Field name made lowercase.
    issued = models.DateTimeField(
        db_column="ISSUED", blank=True, null=True
    )  # Field name made lowercase.
    neighborhood = models.TextField(
        db_column="NEIGHBORHOOD", blank=True, null=True
    )  # Field name made lowercase.
    neighborhood_coalition = models.TextField(
        db_column="NEIGHBORHOOD_COALITION", blank=True, null=True
    )  # Field name made lowercase.
    business_association = models.TextField(
        db_column="BUSINESS_ASSOCIATION", blank=True, null=True
    )  # Field name made lowercase.
    county_y = models.TextField(
        db_column="COUNTY_y", blank=True, null=True
    )  # Field name made lowercase.
    x_web_mercator = models.FloatField(
        db_column="X_WEB_MERCATOR", blank=True, null=True
    )  # Field name made lowercase.
    y_web_mercator = models.FloatField(
        db_column="Y_WEB_MERCATOR", blank=True, null=True
    )  # Field name made lowercase.
    ccb_number = models.TextField(
        db_column="CCB_NUMBER", blank=True, null=True
    )  # Field name made lowercase.
    occupancy_group = models.TextField(
        db_column="OCCUPANCY_GROUP", blank=True, null=True
    )  # Field name made lowercase.
    construction_type = models.TextField(
        db_column="CONSTRUCTION_TYPE", blank=True, null=True
    )  # Field name made lowercase.
    submitted_valuation = models.FloatField(
        db_column="SUBMITTED_VALUATION", blank=True, null=True
    )  # Field name made lowercase.
    final_valuation = models.FloatField(
        db_column="FINAL_VALUATION", blank=True, null=True
    )  # Field name made lowercase.
    new_units = models.FloatField(
        db_column="NEW_UNITS", blank=True, null=True
    )  # Field name made lowercase.
    total_sqft = models.FloatField(
        db_column="TOTAL_SQFT", blank=True, null=True
    )  # Field name made lowercase.
    stories = models.FloatField(
        db_column="STORIES", blank=True, null=True
    )  # Field name made lowercase.
    customer = models.FloatField(
        db_column="CUSTOMER", blank=True, null=True
    )  # Field name made lowercase.
    days_from_issued_to_final = models.FloatField(blank=True, null=True)
    permit_month = models.FloatField(blank=True, null=True)
    permit_year = models.FloatField(blank=True, null=True)
    address_unit_a = models.BooleanField(
        db_column="address_unit_A", blank=True, null=True
    )  # Field name made lowercase.
    sale_year = models.FloatField(blank=True, null=True)
    sale_month = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "joined_adu_permits_to_taxlots"


class Layer(models.Model):
    topology = models.OneToOneField("Topology", models.DO_NOTHING, primary_key=True)
    layer_id = models.IntegerField()
    schema_name = models.CharField(max_length=1)
    table_name = models.CharField(max_length=1)
    feature_column = models.CharField(max_length=1)
    feature_type = models.IntegerField()
    level = models.IntegerField()
    child_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "layer"
        unique_together = (
            ("topology", "layer_id"),
            ("schema_name", "table_name", "feature_column"),
        )


class LrtStop(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    station = models.TextField(
        db_column="STATION", blank=True, null=True
    )  # Field name made lowercase.
    status = models.TextField(
        db_column="STATUS", blank=True, null=True
    )  # Field name made lowercase.
    type = models.TextField(
        db_column="TYPE", blank=True, null=True
    )  # Field name made lowercase.
    line = models.TextField(
        db_column="LINE", blank=True, null=True
    )  # Field name made lowercase.
    geometry = models.PointField(srid=2913, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "lrt_stop"


class MfInventory(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    address = models.TextField(
        db_column="ADDRESS", blank=True, null=True
    )  # Field name made lowercase.
    juris_city = models.TextField(
        db_column="JURIS_CITY", blank=True, null=True
    )  # Field name made lowercase.
    mail_city = models.TextField(
        db_column="MAIL_CITY", blank=True, null=True
    )  # Field name made lowercase.
    state = models.TextField(
        db_column="STATE", blank=True, null=True
    )  # Field name made lowercase.
    units = models.BigIntegerField(
        db_column="UNITS", blank=True, null=True
    )  # Field name made lowercase.
    zipcode = models.TextField(
        db_column="ZIPCODE", blank=True, null=True
    )  # Field name made lowercase.
    unit_type = models.TextField(
        db_column="UNIT_TYPE", blank=True, null=True
    )  # Field name made lowercase.
    county = models.TextField(
        db_column="COUNTY", blank=True, null=True
    )  # Field name made lowercase.
    mixed_use = models.BigIntegerField(
        db_column="MIXED_USE", blank=True, null=True
    )  # Field name made lowercase.
    yearbuilt = models.BigIntegerField(
        db_column="YEARBUILT", blank=True, null=True
    )  # Field name made lowercase.
    commonname = models.TextField(
        db_column="COMMONNAME", blank=True, null=True
    )  # Field name made lowercase.
    datasource = models.TextField(
        db_column="DATASOURCE", blank=True, null=True
    )  # Field name made lowercase.
    confidence = models.TextField(
        db_column="CONFIDENCE", blank=True, null=True
    )  # Field name made lowercase.
    metro_id = models.BigIntegerField(
        db_column="METRO_ID", blank=True, null=True
    )  # Field name made lowercase.
    area = models.FloatField(
        db_column="AREA", blank=True, null=True
    )  # Field name made lowercase.
    geometry = models.GeometryField(srid=2913, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "mf_inventory"


class Parkride(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    station = models.TextField(
        db_column="STATION", blank=True, null=True
    )  # Field name made lowercase.
    address = models.TextField(
        db_column="ADDRESS", blank=True, null=True
    )  # Field name made lowercase.
    city = models.TextField(
        db_column="CITY", blank=True, null=True
    )  # Field name made lowercase.
    zipcode = models.TextField(
        db_column="ZIPCODE", blank=True, null=True
    )  # Field name made lowercase.
    county = models.TextField(
        db_column="COUNTY", blank=True, null=True
    )  # Field name made lowercase.
    owner = models.TextField(
        db_column="OWNER", blank=True, null=True
    )  # Field name made lowercase.
    spaces = models.BigIntegerField(
        db_column="SPACES", blank=True, null=True
    )  # Field name made lowercase.
    status = models.TextField(
        db_column="STATUS", blank=True, null=True
    )  # Field name made lowercase.
    geometry = models.PointField(srid=2913, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "parkride"


class Permits(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    ivr_number = models.BigIntegerField(
        db_column="IVR_NUMBER", blank=True, null=True
    )  # Field name made lowercase.
    application_number = models.TextField(
        db_column="APPLICATION_NUMBER", blank=True, null=True
    )  # Field name made lowercase.
    status = models.TextField(
        db_column="STATUS", blank=True, null=True
    )  # Field name made lowercase.
    type = models.TextField(
        db_column="TYPE", blank=True, null=True
    )  # Field name made lowercase.
    description = models.TextField(
        db_column="DESCRIPTION", blank=True, null=True
    )  # Field name made lowercase.
    work = models.TextField(
        db_column="WORK", blank=True, null=True
    )  # Field name made lowercase.
    address = models.TextField(
        db_column="ADDRESS", blank=True, null=True
    )  # Field name made lowercase.
    state_id = models.TextField(
        db_column="STATE_ID", blank=True, null=True
    )  # Field name made lowercase.
    property_id = models.TextField(
        db_column="PROPERTY_ID", blank=True, null=True
    )  # Field name made lowercase.
    set_up = models.TextField(
        db_column="SET_UP", blank=True, null=True
    )  # Field name made lowercase.
    under_review = models.TextField(
        db_column="UNDER_REVIEW", blank=True, null=True
    )  # Field name made lowercase.
    issued = models.TextField(
        db_column="ISSUED", blank=True, null=True
    )  # Field name made lowercase.
    final = models.TextField(
        db_column="FINAL", blank=True, null=True
    )  # Field name made lowercase.
    neighborhood = models.TextField(
        db_column="NEIGHBORHOOD", blank=True, null=True
    )  # Field name made lowercase.
    neighborhood_coalition = models.TextField(
        db_column="NEIGHBORHOOD_COALITION", blank=True, null=True
    )  # Field name made lowercase.
    business_association = models.TextField(
        db_column="BUSINESS_ASSOCIATION", blank=True, null=True
    )  # Field name made lowercase.
    county = models.TextField(
        db_column="COUNTY", blank=True, null=True
    )  # Field name made lowercase.
    x_web_mercator = models.FloatField(
        db_column="X_WEB_MERCATOR", blank=True, null=True
    )  # Field name made lowercase.
    y_web_mercator = models.FloatField(
        db_column="Y_WEB_MERCATOR", blank=True, null=True
    )  # Field name made lowercase.
    ccb_number = models.TextField(
        db_column="CCB_NUMBER", blank=True, null=True
    )  # Field name made lowercase.
    occupancy_group = models.TextField(
        db_column="OCCUPANCY_GROUP", blank=True, null=True
    )  # Field name made lowercase.
    construction_type = models.TextField(
        db_column="CONSTRUCTION_TYPE", blank=True, null=True
    )  # Field name made lowercase.
    submitted_valuation = models.FloatField(
        db_column="SUBMITTED_VALUATION", blank=True, null=True
    )  # Field name made lowercase.
    final_valuation = models.FloatField(
        db_column="FINAL_VALUATION", blank=True, null=True
    )  # Field name made lowercase.
    new_units = models.FloatField(
        db_column="NEW_UNITS", blank=True, null=True
    )  # Field name made lowercase.
    total_sqft = models.FloatField(
        db_column="TOTAL_SQFT", blank=True, null=True
    )  # Field name made lowercase.
    stories = models.FloatField(
        db_column="STORIES", blank=True, null=True
    )  # Field name made lowercase.
    customer = models.FloatField(
        db_column="CUSTOMER", blank=True, null=True
    )  # Field name made lowercase.
    geometry = models.PointField(srid=3857, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "permits"


class PotentialAduParcels(models.Model):
    tlid = models.TextField(
        db_column="TLID", blank=True, null=True
    )  # Field name made lowercase.
    primaccnum = models.TextField(
        db_column="PRIMACCNUM", blank=True, null=True
    )  # Field name made lowercase.
    altaccnum = models.TextField(
        db_column="ALTACCNUM", blank=True, null=True
    )  # Field name made lowercase.
    siteaddr = models.TextField(
        db_column="SITEADDR", blank=True, null=True
    )  # Field name made lowercase.
    sitecity = models.TextField(
        db_column="SITECITY", blank=True, null=True
    )  # Field name made lowercase.
    sitezip = models.TextField(
        db_column="SITEZIP", blank=True, null=True
    )  # Field name made lowercase.
    landval = models.BigIntegerField(
        db_column="LANDVAL", blank=True, null=True
    )  # Field name made lowercase.
    bldgval = models.BigIntegerField(
        db_column="BLDGVAL", blank=True, null=True
    )  # Field name made lowercase.
    totalval = models.BigIntegerField(
        db_column="TOTALVAL", blank=True, null=True
    )  # Field name made lowercase.
    bldgsqft = models.FloatField(
        db_column="BLDGSQFT", blank=True, null=True
    )  # Field name made lowercase.
    a_t_acres = models.FloatField(
        db_column="A_T_ACRES", blank=True, null=True
    )  # Field name made lowercase.
    yearbuilt = models.BigIntegerField(
        db_column="YEARBUILT", blank=True, null=True
    )  # Field name made lowercase.
    saledate = models.TextField(
        db_column="SALEDATE", blank=True, null=True
    )  # Field name made lowercase.
    saleprice = models.BigIntegerField(
        db_column="SALEPRICE", blank=True, null=True
    )  # Field name made lowercase.
    geometry = models.GeometryField(srid=2913, blank=True, null=True)
    index_right = models.FloatField(blank=True, null=True)
    bldg_id = models.TextField(
        db_column="BLDG_ID", blank=True, null=True
    )  # Field name made lowercase.
    state_id = models.TextField(
        db_column="STATE_ID", blank=True, null=True
    )  # Field name made lowercase.
    bldg_numb = models.FloatField(
        db_column="BLDG_NUMB", blank=True, null=True
    )  # Field name made lowercase.
    bldg_addr = models.TextField(
        db_column="BLDG_ADDR", blank=True, null=True
    )  # Field name made lowercase.
    bldg_sqft = models.FloatField(
        db_column="BLDG_SQFT", blank=True, null=True
    )  # Field name made lowercase.
    num_story = models.FloatField(
        db_column="NUM_STORY", blank=True, null=True
    )  # Field name made lowercase.
    num_units = models.FloatField(
        db_column="NUM_UNITS", blank=True, null=True
    )  # Field name made lowercase.
    year_built = models.FloatField(
        db_column="YEAR_BUILT", blank=True, null=True
    )  # Field name made lowercase.
    bldg_footprint_sq_ft = models.FloatField(blank=True, null=True)
    parcel_sqft = models.FloatField(blank=True, null=True)
    geoid = models.TextField(
        db_column="GEOID", blank=True, null=True
    )  # Field name made lowercase.
    one_bed_rent_sf = models.FloatField(blank=True, null=True)
    two_bed_rent_sf = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "potential_adu_parcels"


class Railroad(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    length = models.FloatField(
        db_column="LENGTH", blank=True, null=True
    )  # Field name made lowercase.
    owner_abrv = models.TextField(
        db_column="OWNER_ABRV", blank=True, null=True
    )  # Field name made lowercase.
    owner = models.TextField(
        db_column="OWNER", blank=True, null=True
    )  # Field name made lowercase.
    geometry = models.GeometryField(srid=2913, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "railroad"


class SchoolDistrict(models.Model):
    distno = models.TextField(
        db_column="DISTNO", blank=True, null=True
    )  # Field name made lowercase.
    distname = models.TextField(
        db_column="DISTNAME", blank=True, null=True
    )  # Field name made lowercase.
    distinstid = models.BigIntegerField(
        db_column="DISTINSTID", blank=True, null=True
    )  # Field name made lowercase.
    ncesdistid = models.BigIntegerField(
        db_column="NCESDISTID", blank=True, null=True
    )  # Field name made lowercase.
    area = models.FloatField(
        db_column="AREA", blank=True, null=True
    )  # Field name made lowercase.
    geometry = models.GeometryField(srid=2913, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "school_district"


class Schools(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    school_id = models.BigIntegerField(
        db_column="SCHOOL_ID", blank=True, null=True
    )  # Field name made lowercase.
    schinstid = models.FloatField(
        db_column="SCHINSTID", blank=True, null=True
    )  # Field name made lowercase.
    distinstid = models.FloatField(
        db_column="DISTINSTID", blank=True, null=True
    )  # Field name made lowercase.
    ncesschid = models.FloatField(
        db_column="NCESSCHID", blank=True, null=True
    )  # Field name made lowercase.
    ncesdistid = models.FloatField(
        db_column="NCESDISTID", blank=True, null=True
    )  # Field name made lowercase.
    site_id = models.FloatField(
        db_column="SITE_ID", blank=True, null=True
    )  # Field name made lowercase.
    primaryuse = models.FloatField(
        db_column="PRIMARYUSE", blank=True, null=True
    )  # Field name made lowercase.
    name = models.TextField(
        db_column="NAME", blank=True, null=True
    )  # Field name made lowercase.
    address = models.TextField(
        db_column="ADDRESS", blank=True, null=True
    )  # Field name made lowercase.
    address2 = models.TextField(
        db_column="ADDRESS2", blank=True, null=True
    )  # Field name made lowercase.
    city = models.TextField(
        db_column="CITY", blank=True, null=True
    )  # Field name made lowercase.
    state = models.TextField(
        db_column="STATE", blank=True, null=True
    )  # Field name made lowercase.
    zipcode = models.TextField(
        db_column="ZIPCODE", blank=True, null=True
    )  # Field name made lowercase.
    zip4 = models.TextField(
        db_column="ZIP4", blank=True, null=True
    )  # Field name made lowercase.
    phone = models.TextField(
        db_column="PHONE", blank=True, null=True
    )  # Field name made lowercase.
    level_no = models.BigIntegerField(
        db_column="LEVEL_NO", blank=True, null=True
    )  # Field name made lowercase.
    level_name = models.TextField(
        db_column="LEVEL_NAME", blank=True, null=True
    )  # Field name made lowercase.
    dist_no = models.TextField(
        db_column="DIST_NO", blank=True, null=True
    )  # Field name made lowercase.
    district = models.TextField(
        db_column="DISTRICT", blank=True, null=True
    )  # Field name made lowercase.
    grade = models.TextField(
        db_column="GRADE", blank=True, null=True
    )  # Field name made lowercase.
    type = models.TextField(
        db_column="TYPE", blank=True, null=True
    )  # Field name made lowercase.
    county = models.TextField(
        db_column="COUNTY", blank=True, null=True
    )  # Field name made lowercase.
    updatedate = models.TextField(
        db_column="UPDATEDATE", blank=True, null=True
    )  # Field name made lowercase.
    geometry = models.PointField(srid=2913, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "schools"


class Taxlots(models.Model):
    area = models.FloatField(
        db_column="AREA", blank=True, null=True
    )  # Field name made lowercase.
    tlid = models.TextField(
        db_column="TLID", blank=True, null=True
    )  # Field name made lowercase.
    primaccnum = models.TextField(
        db_column="PRIMACCNUM", blank=True, null=True
    )  # Field name made lowercase.
    altaccnum = models.TextField(
        db_column="ALTACCNUM", blank=True, null=True
    )  # Field name made lowercase.
    ownersort = models.TextField(
        db_column="OWNERSORT", blank=True, null=True
    )  # Field name made lowercase.
    owner1 = models.TextField(
        db_column="OWNER1", blank=True, null=True
    )  # Field name made lowercase.
    owner2 = models.TextField(
        db_column="OWNER2", blank=True, null=True
    )  # Field name made lowercase.
    owneraddr = models.TextField(
        db_column="OWNERADDR", blank=True, null=True
    )  # Field name made lowercase.
    owneraddr2 = models.TextField(
        db_column="OWNERADDR2", blank=True, null=True
    )  # Field name made lowercase.
    ownercity = models.TextField(
        db_column="OWNERCITY", blank=True, null=True
    )  # Field name made lowercase.
    ownerstate = models.TextField(
        db_column="OWNERSTATE", blank=True, null=True
    )  # Field name made lowercase.
    ownerzip = models.TextField(
        db_column="OWNERZIP", blank=True, null=True
    )  # Field name made lowercase.
    siteaddr = models.TextField(
        db_column="SITEADDR", blank=True, null=True
    )  # Field name made lowercase.
    sitecity = models.TextField(
        db_column="SITECITY", blank=True, null=True
    )  # Field name made lowercase.
    sitezip = models.TextField(
        db_column="SITEZIP", blank=True, null=True
    )  # Field name made lowercase.
    landval = models.BigIntegerField(
        db_column="LANDVAL", blank=True, null=True
    )  # Field name made lowercase.
    bldgval = models.BigIntegerField(
        db_column="BLDGVAL", blank=True, null=True
    )  # Field name made lowercase.
    totalval = models.BigIntegerField(
        db_column="TOTALVAL", blank=True, null=True
    )  # Field name made lowercase.
    bldgsqft = models.FloatField(
        db_column="BLDGSQFT", blank=True, null=True
    )  # Field name made lowercase.
    a_t_acres = models.FloatField(
        db_column="A_T_ACRES", blank=True, null=True
    )  # Field name made lowercase.
    yearbuilt = models.BigIntegerField(
        db_column="YEARBUILT", blank=True, null=True
    )  # Field name made lowercase.
    prop_code = models.TextField(
        db_column="PROP_CODE", blank=True, null=True
    )  # Field name made lowercase.
    landuse = models.TextField(
        db_column="LANDUSE", blank=True, null=True
    )  # Field name made lowercase.
    taxcode = models.TextField(
        db_column="TAXCODE", blank=True, null=True
    )  # Field name made lowercase.
    saledate = models.TextField(
        db_column="SALEDATE", blank=True, null=True
    )  # Field name made lowercase.
    saleprice = models.BigIntegerField(
        db_column="SALEPRICE", blank=True, null=True
    )  # Field name made lowercase.
    county = models.TextField(
        db_column="COUNTY", blank=True, null=True
    )  # Field name made lowercase.
    x_coord = models.BigIntegerField(
        db_column="X_COORD", blank=True, null=True
    )  # Field name made lowercase.
    y_coord = models.BigIntegerField(
        db_column="Y_COORD", blank=True, null=True
    )  # Field name made lowercase.
    juris_city = models.TextField(
        db_column="JURIS_CITY", blank=True, null=True
    )  # Field name made lowercase.
    gis_acres = models.FloatField(
        db_column="GIS_ACRES", blank=True, null=True
    )  # Field name made lowercase.
    stateclass = models.TextField(
        db_column="STATECLASS", blank=True, null=True
    )  # Field name made lowercase.
    ortaxlot = models.TextField(
        db_column="ORTAXLOT", blank=True, null=True
    )  # Field name made lowercase.
    geometry = models.GeometryField(srid=2913, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "taxlots"


class TlMany(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    tlid_long = models.TextField(
        db_column="TLID_LONG", blank=True, null=True
    )  # Field name made lowercase.
    tlid = models.TextField(
        db_column="TLID", blank=True, null=True
    )  # Field name made lowercase.
    primaccnum = models.TextField(
        db_column="PRIMACCNUM", blank=True, null=True
    )  # Field name made lowercase.
    altaccnum = models.TextField(
        db_column="ALTACCNUM", blank=True, null=True
    )  # Field name made lowercase.
    ownersort = models.TextField(
        db_column="OWNERSORT", blank=True, null=True
    )  # Field name made lowercase.
    owner1 = models.TextField(
        db_column="OWNER1", blank=True, null=True
    )  # Field name made lowercase.
    owner2 = models.TextField(
        db_column="OWNER2", blank=True, null=True
    )  # Field name made lowercase.
    owneraddr = models.TextField(
        db_column="OWNERADDR", blank=True, null=True
    )  # Field name made lowercase.
    owneraddr2 = models.TextField(
        db_column="OWNERADDR2", blank=True, null=True
    )  # Field name made lowercase.
    ownercity = models.TextField(
        db_column="OWNERCITY", blank=True, null=True
    )  # Field name made lowercase.
    ownerstate = models.TextField(
        db_column="OWNERSTATE", blank=True, null=True
    )  # Field name made lowercase.
    ownerzip = models.TextField(
        db_column="OWNERZIP", blank=True, null=True
    )  # Field name made lowercase.
    siteaddr = models.TextField(
        db_column="SITEADDR", blank=True, null=True
    )  # Field name made lowercase.
    sitecity = models.TextField(
        db_column="SITECITY", blank=True, null=True
    )  # Field name made lowercase.
    sitezip = models.TextField(
        db_column="SITEZIP", blank=True, null=True
    )  # Field name made lowercase.
    landval = models.BigIntegerField(
        db_column="LANDVAL", blank=True, null=True
    )  # Field name made lowercase.
    bldgval = models.BigIntegerField(
        db_column="BLDGVAL", blank=True, null=True
    )  # Field name made lowercase.
    totalval = models.BigIntegerField(
        db_column="TOTALVAL", blank=True, null=True
    )  # Field name made lowercase.
    bldgsqft = models.BigIntegerField(
        db_column="BLDGSQFT", blank=True, null=True
    )  # Field name made lowercase.
    a_t_acres = models.FloatField(
        db_column="A_T_ACRES", blank=True, null=True
    )  # Field name made lowercase.
    yearbuilt = models.BigIntegerField(
        db_column="YEARBUILT", blank=True, null=True
    )  # Field name made lowercase.
    prop_code = models.TextField(
        db_column="PROP_CODE", blank=True, null=True
    )  # Field name made lowercase.
    landuse = models.TextField(
        db_column="LANDUSE", blank=True, null=True
    )  # Field name made lowercase.
    taxcode = models.TextField(
        db_column="TAXCODE", blank=True, null=True
    )  # Field name made lowercase.
    saledate = models.TextField(
        db_column="SALEDATE", blank=True, null=True
    )  # Field name made lowercase.
    saleprice = models.BigIntegerField(
        db_column="SALEPRICE", blank=True, null=True
    )  # Field name made lowercase.
    county = models.TextField(
        db_column="COUNTY", blank=True, null=True
    )  # Field name made lowercase.
    x_coord = models.FloatField(
        db_column="X_COORD", blank=True, null=True
    )  # Field name made lowercase.
    y_coord = models.FloatField(
        db_column="Y_COORD", blank=True, null=True
    )  # Field name made lowercase.
    juris_city = models.TextField(
        db_column="JURIS_CITY", blank=True, null=True
    )  # Field name made lowercase.
    stateclass = models.TextField(
        db_column="STATECLASS", blank=True, null=True
    )  # Field name made lowercase.
    geometry = models.PointField(srid=2913, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "tl_many"


class Topology(models.Model):
    name = models.CharField(unique=True, max_length=1)
    srid = models.IntegerField()
    precision = models.FloatField()
    hasz = models.BooleanField()

    class Meta:
        managed = False
        db_table = "topology"


class Zoning(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    city_no = models.BigIntegerField(
        db_column="CITY_NO", blank=True, null=True
    )  # Field name made lowercase.
    zone = models.TextField(
        db_column="ZONE", blank=True, null=True
    )  # Field name made lowercase.
    zone_class = models.TextField(
        db_column="ZONE_CLASS", blank=True, null=True
    )  # Field name made lowercase.
    zonegen_cl = models.TextField(
        db_column="ZONEGEN_CL", blank=True, null=True
    )  # Field name made lowercase.
    city = models.TextField(
        db_column="CITY", blank=True, null=True
    )  # Field name made lowercase.
    area = models.FloatField(
        db_column="AREA", blank=True, null=True
    )  # Field name made lowercase.
    geometry = models.GeometryField(srid=2913, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "zoning"
