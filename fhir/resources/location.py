# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Location
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from typing import List as ListType
from typing import Union

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class Location(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Details and position information for a physical place.
    Details and position information for a physical place where services are
    provided and resources and participants may be stored, found, contained, or
    accommodated.
    """

    resource_type = Field("Location", const=True)

    address: fhirtypes.AddressType = Field(
        None,
        alias="address",
        title="Physical location",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    alias: ListType[fhirtypes.String] = Field(
        None,
        alias="alias",
        title=(
            "A list of alternate names that the location is known as, or was known "
            "as, in the past"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    alias__ext: ListType[Union[fhirtypes.FHIRPrimitiveExtensionType, None]] = Field(
        None, alias="_alias", title="Extension field for ``alias``."
    )

    availabilityExceptions: fhirtypes.String = Field(
        None,
        alias="availabilityExceptions",
        title="Description of availability exceptions",
        description=(
            "A description of when the locations opening ours are different to "
            "normal, e.g. public holiday availability. Succinctly describing all "
            "possible exceptions to normal site availability as detailed in the "
            "opening hours Times."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    availabilityExceptions__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_availabilityExceptions",
        title="Extension field for ``availabilityExceptions``.",
    )

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title=(
            "Additional details about the location that could be displayed as "
            "further information to identify the location beyond its name"
        ),
        description=(
            "Description of the Location, which helps in finding or referencing the"
            " place."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    endpoint: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="endpoint",
        title=(
            "Technical endpoints providing access to services operated for the "
            "location"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Endpoint"],
    )

    hoursOfOperation: ListType[fhirtypes.LocationHoursOfOperationType] = Field(
        None,
        alias="hoursOfOperation",
        title="What days/times during a week is this location usually open",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="Unique code or number identifying the location to its users",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    managingOrganization: fhirtypes.ReferenceType = Field(
        None,
        alias="managingOrganization",
        title="Organization responsible for provisioning and upkeep",
        description=(
            "The organization responsible for the provisioning and upkeep of the "
            "location."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization"],
    )

    mode: fhirtypes.Code = Field(
        None,
        alias="mode",
        title="instance | kind",
        description=(
            "Indicates whether a resource instance represents a specific location "
            "or a class of locations."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["instance", "kind"],
    )
    mode__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_mode", title="Extension field for ``mode``."
    )

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Name of the location as used by humans",
        description="Name of the location as used by humans. Does not need to be unique.",
        # if property is element of this resource.
        element_property=True,
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )

    operationalStatus: fhirtypes.CodingType = Field(
        None,
        alias="operationalStatus",
        title="The operational status of the location (typically only for a bed/room)",
        description=(
            "The operational status covers operation values most relevant to beds "
            "(but can also apply to rooms/units/chairs/etc. such as an isolation "
            "unit/dialysis chair). This typically covers concepts such as "
            "contamination, housekeeping, and other activities like maintenance."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    partOf: fhirtypes.ReferenceType = Field(
        None,
        alias="partOf",
        title="Another Location this one is physically a part of",
        description="Another Location of which this Location is physically a part of.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Location"],
    )

    physicalType: fhirtypes.CodeableConceptType = Field(
        None,
        alias="physicalType",
        title="Physical form of the location",
        description="Physical form of the location, e.g. building, room, vehicle, road.",
        # if property is element of this resource.
        element_property=True,
    )

    position: fhirtypes.LocationPositionType = Field(
        None,
        alias="position",
        title="The absolute geographic location",
        description=(
            "The absolute geographic location of the Location, expressed using the "
            "WGS84 datum (This is the same co-ordinate system used in KML)."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title="active | suspended | inactive",
        description=(
            "The status property covers the general availability of the resource, "
            "not the current value which may be covered by the operationStatus, or "
            "by a schedule/slots if they are configured for the location."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["active", "suspended", "inactive"],
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )

    telecom: ListType[fhirtypes.ContactPointType] = Field(
        None,
        alias="telecom",
        title="Contact details of the location",
        description=(
            "The contact details of communication devices available at the "
            "location. This can include phone numbers, fax numbers, mobile numbers,"
            " email addresses and web sites."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    type: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="type",
        title="Type of function performed",
        description="Indicates the type of function performed at the location.",
        # if property is element of this resource.
        element_property=True,
    )


class LocationHoursOfOperation(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    What days/times during a week is this location usually open.
    """

    resource_type = Field("LocationHoursOfOperation", const=True)

    allDay: bool = Field(
        None,
        alias="allDay",
        title="The Location is open all day",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    allDay__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_allDay", title="Extension field for ``allDay``."
    )

    closingTime: fhirtypes.Time = Field(
        None,
        alias="closingTime",
        title="Time that the Location closes",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    closingTime__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_closingTime", title="Extension field for ``closingTime``."
    )

    daysOfWeek: ListType[fhirtypes.Code] = Field(
        None,
        alias="daysOfWeek",
        title="mon | tue | wed | thu | fri | sat | sun",
        description=(
            "Indicates which days of the week are available between the start and "
            "end Times."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["mon", "tue", "wed", "thu", "fri", "sat", "sun"],
    )
    daysOfWeek__ext: ListType[
        Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(None, alias="_daysOfWeek", title="Extension field for ``daysOfWeek``.")

    openingTime: fhirtypes.Time = Field(
        None,
        alias="openingTime",
        title="Time that the Location opens",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    openingTime__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_openingTime", title="Extension field for ``openingTime``."
    )


class LocationPosition(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The absolute geographic location.
    The absolute geographic location of the Location, expressed using the WGS84
    datum (This is the same co-ordinate system used in KML).
    """

    resource_type = Field("LocationPosition", const=True)

    altitude: fhirtypes.Decimal = Field(
        None,
        alias="altitude",
        title="Altitude with WGS84 datum",
        description=(
            "Altitude. The value domain and the interpretation are the same as for "
            "the text of the altitude element in KML (see notes below)."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    altitude__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_altitude", title="Extension field for ``altitude``."
    )

    latitude: fhirtypes.Decimal = Field(
        ...,
        alias="latitude",
        title="Latitude with WGS84 datum",
        description=(
            "Latitude. The value domain and the interpretation are the same as for "
            "the text of the latitude element in KML (see notes below)."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    latitude__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_latitude", title="Extension field for ``latitude``."
    )

    longitude: fhirtypes.Decimal = Field(
        ...,
        alias="longitude",
        title="Longitude with WGS84 datum",
        description=(
            "Longitude. The value domain and the interpretation are the same as for"
            " the text of the longitude element in KML (see notes below)."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    longitude__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_longitude", title="Extension field for ``longitude``."
    )
