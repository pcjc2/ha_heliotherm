"""Constants for the HaHeliotherm integration."""

from dataclasses import dataclass
from homeassistant.components.climate import (
    ClimateEntityDescription,
    ClimateEntityFeature,
)

from homeassistant.components.sensor import *

from homeassistant.components.binary_sensor import (
    BinarySensorDeviceClass,
    BinarySensorEntity,
    BinarySensorEntityDescription,
)

from homeassistant.components.number import (
    NumberEntity,
    NumberEntityDescription,
    NumberDeviceClass,
)
from homeassistant.const import UnitOfPressure, UnitOfTemperature, CONF_NAME

# from homeassistant.const import *

DOMAIN = "ha_heliotherm"
DEFAULT_NAME = "Heliotherm Heatpump"
DEFAULT_SCAN_INTERVAL = 15
DEFAULT_PORT = 502
DEFAULT_HOSTID = 1
CONF_HOSTID = "hostid"
CONF_HALEIOTHERM_HUB = "haheliotherm_hub"
ATTR_MANUFACTURER = "Heliotherm"


@dataclass
class HaHeliothermNumberEntityDescription(NumberEntityDescription):
    """A class that describes HaHeliotherm Modbus sensor entities."""

    mode: str = "slider"
    initial: float = None
    editable: bool = True


@dataclass
class HaHeliothermSensorEntityDescription(SensorEntityDescription):
    """A class that describes HaHeliotherm Modbus sensor entities."""


@dataclass
class HaHeliothermBinarySensorEntityDescription(BinarySensorEntityDescription):
    """A class that describes HaHeliotherm Modbus binarysensor entities."""


@dataclass
class HaHeliothermSelectEntityDescription(SensorEntityDescription):
    """A class that describes HaHeliotherm Modbus binarysensor entities."""

    select_options: list[str] = None
    default_select_option: str = None
    setter_function = None


@dataclass
class HaHeliothermClimateEntityDescription(ClimateEntityDescription):
    """A class that describes HaHeliotherm Modbus binarysensor entities."""

    min_value: float = None
    max_value: float = None
    step: float = None
    hvac_modes: list[str] = None
    temperature_unit: str = "°C"
    supported_features: ClimateEntityFeature = ClimateEntityFeature.TARGET_TEMPERATURE


CLIMATE_TYPES: dict[str, list[HaHeliothermClimateEntityDescription]] = {
    "climate_hkr_raum_soll": HaHeliothermClimateEntityDescription(
        name="Raum Solltemperatur",
        key="climate_hkr_raum_soll",
        min_value=10,
        max_value=25,
        step=0.5,
        temperature_unit="°C",
    ),
    "climate_rlt_kuehlen": HaHeliothermClimateEntityDescription(
        name="Kühlen RLT Soll",
        key="climate_rlt_kuehlen",
        min_value=15,
        max_value=25,
        step=1,
        temperature_unit="°C",
    ),
    "climate_ww_bereitung": HaHeliothermClimateEntityDescription(
        name="Warmwasserbereitung",
        key="climate_ww_bereitung",
        min_value=5,
        max_value=65,
        step=0.5,
        temperature_unit="°C",
        supported_features=ClimateEntityFeature.TARGET_TEMPERATURE_RANGE,
    ),

#---------------------eingefügt-------------------------------------------------
    "climate_rl_soll": HaHeliothermClimateEntityDescription(
        name="Rücklaufsolltemperatur",
        key="climate_rl_soll",
        min_value=5,
        max_value=65,
        step=0.5,
        temperature_unit="°C",
        supported_features=ClimateEntityFeature.TARGET_TEMPERATURE
        #----hier keine Range, sondern fester Wert-------
    ),
#---------------------eingefügt-------------------------------------------------
#-------------hs/ategus: begin
    "climate_mkr1_raum_soll": HaHeliothermClimateEntityDescription(
        name="MKR1 Solltemperatur",
        key="climate_mkr1_raum_soll",
        min_value=10,
        max_value=25,
        step=0.5,
        temperature_unit="°C",
    ),
    "climate_mkr1_rl_soll": HaHeliothermClimateEntityDescription(
        name="MKR1 Rücklaufsolltemperatur",
        key="climate_mkr1_rl_soll",
        min_value=5,
        max_value=65,
        step=0.5,
        temperature_unit="°C",
        supported_features=ClimateEntityFeature.TARGET_TEMPERATURE
        #----hier keine Range, sondern fester Wert-------
    ),
    "climate_mkr1_rlt_kuehlen": HaHeliothermClimateEntityDescription(
        name="Kühlen MKR1 RLT Soll",
        key="climate_mkr1_rlt_kuehlen",
        min_value=15,
        max_value=25,
        step=1,
        temperature_unit="°C",
    ),
    "climate_mkr2_raum_soll": HaHeliothermClimateEntityDescription(
        name="MKR2 Solltemperatur",
        key="climate_mkr2_raum_soll",
        min_value=10,
        max_value=25,
        step=0.5,
        temperature_unit="°C",
    ),
    "climate_mkr2_rl_soll": HaHeliothermClimateEntityDescription(
        name="MKR2 Rücklaufsolltemperatur",
        key="climate_mkr2_rl_soll",
        min_value=5,
        max_value=65,
        step=0.5,
        temperature_unit="°C",
        supported_features=ClimateEntityFeature.TARGET_TEMPERATURE
        #----hier keine Range, sondern fester Wert-------
    ),
    "climate_mkr2_rlt_kuehlen": HaHeliothermClimateEntityDescription(
        name="Kühlen MKR2 RLT Soll",
        key="climate_mkr2_rlt_kuehlen",
        min_value=15,
        max_value=25,
        step=1,
        temperature_unit="°C",
    ),
    "climate_pv_heizen_offset": HaHeliothermClimateEntityDescription(
        name="PV Heizen Offset",
        key="climate_pv_heizen_offset",
        min_value=0,
        max_value=10,
        step=0.1,
        temperature_unit="K",
    ),
    "climate_pv_kuehlen_offset": HaHeliothermClimateEntityDescription(
        name="PV Kühlen Offset",
        key="climate_pv_kuehlen_offset",
        min_value=0,
        max_value=10,
        step=0.1,
        temperature_unit="K",
    ),
    "climate_mkr1_pv_heizen_offset": HaHeliothermClimateEntityDescription(
        name="PV Heizen Offset MKR1",
        key="climate_mkr1_pv_heizen_offset",
        min_value=0,
        max_value=10,
        step=0.1,
        temperature_unit="K",
    ),
    "climate_mkr1_pv_kuehlen_offset": HaHeliothermClimateEntityDescription(
        name="PV Kühlen Offset MKR1",
        key="climate_mkr1_pv_kuehlen_offset",
        min_value=0,
        max_value=10,
        step=0.1,
        temperature_unit="K",
    ),

    "climate_mkr2_pv_heizen_offset": HaHeliothermClimateEntityDescription(
        name="PV Heizen Offset MKR2",
        key="climate_mkr2_pv_heizen_offset",
        min_value=0,
        max_value=10,
        step=0.1,
        temperature_unit="K",
    ),
    "climate_mkr2_pv_kuehlen_offset": HaHeliothermClimateEntityDescription(
        name="PV Kühlen Offset MKR2",
        key="climate_mkr2_pv_kuehlen_offset",
        min_value=0,
        max_value=10,
        step=0.1,
        temperature_unit="K",
    ),


#---------------------eingefügt-------------------------------------------------

#-------------hs/ategus: Ende
}

NUMBER_TYPES: dict[str, list[HaHeliothermNumberEntityDescription]] = {}

SELECT_TYPES: dict[str, list[HaHeliothermSelectEntityDescription]] = {
    "select_betriebsart": HaHeliothermSelectEntityDescription(
        name="Betriebsart",
        key="select_betriebsart",
        select_options=[
            "Aus",
            "Auto",
            "Kühlen",
            "Sommer",
            "Dauerbetrieb",
            "Absenken",
            "Urlaub",
            "Party",
        ],
        default_select_option="Auto",
    ),
    "select_mkr1_betriebsart": HaHeliothermSelectEntityDescription(
        name="MKR 1 Betriebsart",
        key="select_mkr1_betriebsart",
        select_options=[
            "Aus",
            "Auto",
            "Kühlen",
            "Sommer",
            "Dauerbetrieb",
            "Absenken",
            "Urlaub",
            "Party",
        ],
        default_select_option="Auto",
    ),
    "select_mkr2_betriebsart": HaHeliothermSelectEntityDescription(
        name="MKR 2 Betriebsart",
        key="select_mkr2_betriebsart",
        select_options=[
            "Aus",
            "Auto",
            "Kühlen",
            "Sommer",
            "Dauerbetrieb",
            "Absenken",
            "Urlaub",
            "Party",
        ],
        default_select_option="Auto",
    ),
}

SENSOR_TYPES: dict[str, list[HaHeliothermSensorEntityDescription]] = {
    "temp_aussen": HaHeliothermSensorEntityDescription(
        name="Temp. Aussen",
        key="temp_aussen",
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        device_class=SensorDeviceClass.TEMPERATURE,
    ),
    "temp_brauchwasser": HaHeliothermSensorEntityDescription(
        name="Temp. Brauchwasser",
        key="temp_brauchwasser",
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        device_class=SensorDeviceClass.TEMPERATURE,
    ),
    "temp_vorlauf": HaHeliothermSensorEntityDescription(
        name="Temp. Vorlauf",
        key="temp_vorlauf",
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        device_class=SensorDeviceClass.TEMPERATURE,
    ),
    "temp_ruecklauf": HaHeliothermSensorEntityDescription(
        name="Temp. Rücklauf",
        key="temp_ruecklauf",
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        device_class=SensorDeviceClass.TEMPERATURE,
    ),
    "temp_pufferspeicher": HaHeliothermSensorEntityDescription(
        name="Temp. Pufferspeicher",
        key="temp_pufferspeicher",
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        device_class=SensorDeviceClass.TEMPERATURE,
    ),
    "temp_eq_eintritt": HaHeliothermSensorEntityDescription(
        name="Temp. EQ Eintritt",
        key="temp_eq_eintritt",
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        device_class=SensorDeviceClass.TEMPERATURE,
    ),
    "temp_eq_austritt": HaHeliothermSensorEntityDescription(
        name="Temp. EQ Austritt",
        key="temp_eq_austritt",
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        device_class=SensorDeviceClass.TEMPERATURE,
    ),
    "temp_sauggas": HaHeliothermSensorEntityDescription(
        name="Temp. Sauggas",
        key="temp_sauggas",
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        device_class=SensorDeviceClass.TEMPERATURE,
    ),
    "temp_verdampfung": HaHeliothermSensorEntityDescription(
        name="Temp. Verdampfung",
        key="temp_verdampfung",
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        device_class=SensorDeviceClass.TEMPERATURE,
    ),
    "temp_kodensation": HaHeliothermSensorEntityDescription(
        name="Temp. Kondensation",
        key="temp_kodensation",
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        device_class=SensorDeviceClass.TEMPERATURE,
    ),
    "temp_heissgas": HaHeliothermSensorEntityDescription(
        name="Temp. Heissgas",
        key="temp_heissgas",
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        device_class=SensorDeviceClass.TEMPERATURE,
    ),
    "bar_niederdruck": HaHeliothermSensorEntityDescription(
        name="Niederdruck (bar)",
        key="bar_niederdruck",
        native_unit_of_measurement=UnitOfPressure.BAR,
        device_class=SensorDeviceClass.PRESSURE,
    ),
    "bar_hochdruck": HaHeliothermSensorEntityDescription(
        name="Hochdruck (bar)",
        key="bar_hochdruck",
        native_unit_of_measurement=UnitOfPressure.BAR,
        device_class=SensorDeviceClass.PRESSURE,
    ),
    "vierwegeventil_luft": HaHeliothermSensorEntityDescription(
        name="Vierwegeventil Luft",
        key="vierwegeventil_luft",
    ),
    "wmz_durchfluss": HaHeliothermSensorEntityDescription(
        name="WMZ_Durchfluss",
        key="wmz_durchfluss",
        native_unit_of_measurement="l/min",
    ),
    "n_soll_verdichter": HaHeliothermSensorEntityDescription(
        name="n-Soll Verdichter",
        key="n_soll_verdichter",
        native_unit_of_measurement="‰",
    ),
    "cop": HaHeliothermSensorEntityDescription(
        name="COP",
        key="cop",
        native_unit_of_measurement="",
    ),
    "temp_frischwasser": HaHeliothermSensorEntityDescription(
        name="Temp. Frischwasser",
        key="temp_frischwasser",
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        device_class=SensorDeviceClass.TEMPERATURE,
    ),
    "temp_aussen_verzoegert": HaHeliothermSensorEntityDescription(
        name="Temp. Aussen verzögert",
        key="temp_aussen_verzoegert",
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        device_class=SensorDeviceClass.TEMPERATURE,
    ),
    "hkr_solltemperatur": HaHeliothermSensorEntityDescription(
        name="HKR Soll Temperatur",
        key="hkr_solltemperatur",
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        device_class=SensorDeviceClass.TEMPERATURE,
    ),
    "mkr1_solltemperatur": HaHeliothermSensorEntityDescription(
        name="MKR1 Soll Temperatur",
        key="mkr1_solltemperatur",
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        device_class=SensorDeviceClass.TEMPERATURE,
    ),
    "mkr2_solltemperatur": HaHeliothermSensorEntityDescription(
        name="MKR2 Soll Temperatur",
        key="mkr2_solltemperatur",
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        device_class=SensorDeviceClass.TEMPERATURE,
    ),
    "expansionsventil": HaHeliothermSensorEntityDescription(
        name="Expansionsventil",
        key="expansionsventil",
        native_unit_of_measurement="‰",
    ),
    "verdichteranforderung": HaHeliothermSensorEntityDescription(
        name="Anforderung",
        key="verdichteranforderung",
    ),
# HS/ategus: zugefügt
    "betriebsstunden_ww": HaHeliothermSensorEntityDescription(
        name="Betriebsstunden Warmwasser",
        key="betriebsstunden_ww",
        native_unit_of_measurement="h",
        device_class=SensorDeviceClass.DURATION,
        state_class=SensorStateClass.TOTAL_INCREASING,
    ),
    "betriebsstunden_hzg": HaHeliothermSensorEntityDescription(
        name="Betriebsstunden Heizung",
        key="betriebsstunden_hzg",
        native_unit_of_measurement="h",
        device_class=SensorDeviceClass.DURATION,
        state_class=SensorStateClass.TOTAL_INCREASING,
    ),
    "mkr1_vorlauftemperatur": HaHeliothermSensorEntityDescription(
        name="MKR1 Vorlauf Temperatur",
        key="mkr1_vorlauftemperatur",
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        device_class=SensorDeviceClass.TEMPERATURE,
    ),
    "mkr2_vorlauftemperatur": HaHeliothermSensorEntityDescription(
        name="MKR2 Vorlauf Temperatur",
        key="mkr2_vorlauftemperatur",
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        device_class=SensorDeviceClass.TEMPERATURE,
    ),
    "mkr1_ruecklauftemperatur": HaHeliothermSensorEntityDescription(
        name="MKR1 Rücklauf Temperatur",
        key="mkr1_ruecklauftemperatur",
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        device_class=SensorDeviceClass.TEMPERATURE,
    ),
    "mkr2_ruecklauftemperatur": HaHeliothermSensorEntityDescription(
        name="MKR2 Rücklauf Temperatur",
        key="mkr2_ruecklauftemperatur",
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        device_class=SensorDeviceClass.TEMPERATURE,
    ),
    "raumfuehler1_temperatur": HaHeliothermSensorEntityDescription(
        name="Raumfühler 1 Temperatur",
        key="raumfuehler1_temperatur",
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        device_class=SensorDeviceClass.TEMPERATURE,
    ),

# Ende zugefügt
    "wmz_heizung": HaHeliothermSensorEntityDescription(
        name="WMZ Heizung",
        key="wmz_heizung",
        native_unit_of_measurement="kWh",
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
    ),
    "stromz_heizung": HaHeliothermSensorEntityDescription(
        name="Stromzähler Heizung",
        key="stromz_heizung",
        native_unit_of_measurement="kWh",
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
    ),
    "wmz_brauchwasser": HaHeliothermSensorEntityDescription(
        name="WMZ Brauchwasser",
        key="wmz_brauchwasser",
        native_unit_of_measurement="kWh",
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
    ),
    "stromz_brauchwasser": HaHeliothermSensorEntityDescription(
        name="Stromzähler Brauchwasser",
        key="stromz_brauchwasser",
        native_unit_of_measurement="kWh",
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
    ),
    "stromz_gesamt": HaHeliothermSensorEntityDescription(
        name="Stromzähler Gesamt",
        key="stromz_gesamt",
        native_unit_of_measurement="kWh",
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
    ),
    "stromz_leistung": HaHeliothermSensorEntityDescription(
        name="Stromzähler Leistung",
        key="stromz_leistung",
        native_unit_of_measurement="W",
        device_class=SensorDeviceClass.POWER,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    "wmz_gesamt": HaHeliothermSensorEntityDescription(
        name="WMZ Gesamt",
        key="wmz_gesamt",
        native_unit_of_measurement="kWh",
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
    ),
    "wmz_leistung": HaHeliothermSensorEntityDescription(
        name="WMZ Leistung",
        key="wmz_leistung",
        native_unit_of_measurement="kW",
        device_class=SensorDeviceClass.POWER,
        state_class=SensorStateClass.MEASUREMENT,
    ),
}


BINARYSENSOR_TYPES: dict[str, list[HaHeliothermBinarySensorEntityDescription]] = {
    "on_off_heizkreispumpe": HaHeliothermBinarySensorEntityDescription(
        name="Heizkreispumpe",
        key="on_off_heizkreispumpe",
    ),
    "on_off_pufferladepumpe": HaHeliothermBinarySensorEntityDescription(
        name="Pufferladepumpe",
        key="on_off_pufferladepumpe",
    ),
    "on_off_verdichter": HaHeliothermBinarySensorEntityDescription(
        name="Verdichter",
        key="on_off_verdichter",
    ),
    "on_off_stoerung": HaHeliothermBinarySensorEntityDescription(
        name="Stoerung",
        key="on_off_stoerung",
    ),
    "on_off_evu_sperre": HaHeliothermBinarySensorEntityDescription(
        name="EVU Sperre",
        key="on_off_evu_sperre",
    ),
    "on_off_eq_ventilator": HaHeliothermBinarySensorEntityDescription(
        name="EQ Ventilator",
        key="on_off_eq_ventilator",
    ),
    "ww_vorrang": HaHeliothermBinarySensorEntityDescription(
        name="WW Vorrang",
        key="ww_vorrang",
    ),
    "kuehlen_umv_passiv": HaHeliothermBinarySensorEntityDescription(
        name="Kühlen UMV passiv",
        key="kuehlen_umv_passiv",
    ),
}
