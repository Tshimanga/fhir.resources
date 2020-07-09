# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/VerificationResult
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from typing import List as ListType
from typing import Union

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class VerificationResult(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Describes validation requirements, source(s), status and dates for one or
    more elements.
    """

    resource_type = Field("VerificationResult", const=True)

    attestation: fhirtypes.VerificationResultAttestationType = Field(
        None,
        alias="attestation",
        title="Information about the entity attesting to information",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    failureAction: fhirtypes.CodeableConceptType = Field(
        None,
        alias="failureAction",
        title="fatal | warn | rec-only | none",
        description="The result if validation fails (fatal; warning; record only; none).",
        # if property is element of this resource.
        element_property=True,
    )

    frequency: fhirtypes.TimingType = Field(
        None,
        alias="frequency",
        title="Frequency of revalidation",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    lastPerformed: fhirtypes.DateTime = Field(
        None,
        alias="lastPerformed",
        title=(
            "The date/time validation was last completed (including failed "
            "validations)"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    lastPerformed__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_lastPerformed", title="Extension field for ``lastPerformed``."
    )

    need: fhirtypes.CodeableConceptType = Field(
        None,
        alias="need",
        title="none | initial | periodic",
        description=(
            "The frequency with which the target must be validated (none; initial; "
            "periodic)."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    nextScheduled: fhirtypes.Date = Field(
        None,
        alias="nextScheduled",
        title="The date when target is next validated, if appropriate",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    nextScheduled__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_nextScheduled", title="Extension field for ``nextScheduled``."
    )

    primarySource: ListType[fhirtypes.VerificationResultPrimarySourceType] = Field(
        None,
        alias="primarySource",
        title="Information about the primary source(s) involved in validation",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    status: fhirtypes.Code = Field(
        ...,
        alias="status",
        title=(
            "attested | validated | in-process | req-revalid | val-fail | reval-" "fail"
        ),
        description=(
            "The validation status of the target (attested; validated; in process; "
            "requires revalidation; validation failed; revalidation failed)."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=[
            "attested",
            "validated",
            "in-process",
            "req-revalid",
            "val-fail",
            "reval-fail",
        ],
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )

    statusDate: fhirtypes.DateTime = Field(
        None,
        alias="statusDate",
        title="When the validation status was updated",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    statusDate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_statusDate", title="Extension field for ``statusDate``."
    )

    target: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="target",
        title="A resource that was validated",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Resource"],
    )

    targetLocation: ListType[fhirtypes.String] = Field(
        None,
        alias="targetLocation",
        title="The fhirpath location(s) within the resource that was validated",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    targetLocation__ext: ListType[
        Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(
        None, alias="_targetLocation", title="Extension field for ``targetLocation``."
    )

    validationProcess: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="validationProcess",
        title=(
            "The primary process by which the target is validated (edit check; "
            "value set; primary source; multiple sources; standalone; in context)"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    validationType: fhirtypes.CodeableConceptType = Field(
        None,
        alias="validationType",
        title="nothing | primary | multiple",
        description=(
            "What the target is validated against (nothing; primary source; "
            "multiple sources)."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    validator: ListType[fhirtypes.VerificationResultValidatorType] = Field(
        None,
        alias="validator",
        title="Information about the entity validating information",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )


class VerificationResultAttestation(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Information about the entity attesting to information.
    """

    resource_type = Field("VerificationResultAttestation", const=True)

    communicationMethod: fhirtypes.CodeableConceptType = Field(
        None,
        alias="communicationMethod",
        title="The method by which attested information was submitted/retrieved",
        description=(
            "The method by which attested information was submitted/retrieved "
            "(manual; API; Push)."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    date: fhirtypes.Date = Field(
        None,
        alias="date",
        title="The date the information was attested to",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    date__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_date", title="Extension field for ``date``."
    )

    onBehalfOf: fhirtypes.ReferenceType = Field(
        None,
        alias="onBehalfOf",
        title=(
            "When the who is asserting on behalf of another (organization or "
            "individual)"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization", "Practitioner", "PractitionerRole"],
    )

    proxyIdentityCertificate: fhirtypes.String = Field(
        None,
        alias="proxyIdentityCertificate",
        title=(
            "A digital identity certificate associated with the proxy entity "
            "submitting attested information on behalf of the attestation source"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    proxyIdentityCertificate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_proxyIdentityCertificate",
        title="Extension field for ``proxyIdentityCertificate``.",
    )

    proxySignature: fhirtypes.SignatureType = Field(
        None,
        alias="proxySignature",
        title="Proxy signature",
        description=(
            "Signed assertion by the proxy entity indicating that they have the "
            "right to submit attested information on behalf of the attestation "
            "source."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    sourceIdentityCertificate: fhirtypes.String = Field(
        None,
        alias="sourceIdentityCertificate",
        title="A digital identity certificate associated with the attestation source",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    sourceIdentityCertificate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_sourceIdentityCertificate",
        title="Extension field for ``sourceIdentityCertificate``.",
    )

    sourceSignature: fhirtypes.SignatureType = Field(
        None,
        alias="sourceSignature",
        title="Attester signature",
        description=(
            "Signed assertion by the attestation source that they have attested to "
            "the information."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    who: fhirtypes.ReferenceType = Field(
        None,
        alias="who",
        title="The individual or organization attesting to information",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Practitioner", "PractitionerRole", "Organization"],
    )


class VerificationResultPrimarySource(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Information about the primary source(s) involved in validation.
    """

    resource_type = Field("VerificationResultPrimarySource", const=True)

    canPushUpdates: fhirtypes.CodeableConceptType = Field(
        None,
        alias="canPushUpdates",
        title="yes | no | undetermined",
        description=(
            "Ability of the primary source to push updates/alerts (yes; no; "
            "undetermined)."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    communicationMethod: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="communicationMethod",
        title="Method for exchanging information with the primary source",
        description="Method for communicating with the primary source (manual; API; Push).",
        # if property is element of this resource.
        element_property=True,
    )

    pushTypeAvailable: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="pushTypeAvailable",
        title="specific | any | source",
        description=(
            "Type of alerts/updates the primary source can send (specific requested"
            " changes; any changes; as defined by source)."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    type: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="type",
        title=(
            "Type of primary source (License Board; Primary Education; Continuing "
            "Education; Postal Service; Relationship owner; Registration Authority;"
            " legal source; issuing source; authoritative source)"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    validationDate: fhirtypes.DateTime = Field(
        None,
        alias="validationDate",
        title="When the target was validated against the primary source",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    validationDate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_validationDate", title="Extension field for ``validationDate``."
    )

    validationStatus: fhirtypes.CodeableConceptType = Field(
        None,
        alias="validationStatus",
        title="successful | failed | unknown",
        description=(
            "Status of the validation of the target against the primary source "
            "(successful; failed; unknown)."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    who: fhirtypes.ReferenceType = Field(
        None,
        alias="who",
        title="Reference to the primary source",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization", "Practitioner", "PractitionerRole"],
    )


class VerificationResultValidator(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Information about the entity validating information.
    """

    resource_type = Field("VerificationResultValidator", const=True)

    attestationSignature: fhirtypes.SignatureType = Field(
        None,
        alias="attestationSignature",
        title="Validator signature",
        description=(
            "Signed assertion by the validator that they have validated the "
            "information."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    identityCertificate: fhirtypes.String = Field(
        None,
        alias="identityCertificate",
        title="A digital identity certificate associated with the validator",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    identityCertificate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_identityCertificate",
        title="Extension field for ``identityCertificate``.",
    )

    organization: fhirtypes.ReferenceType = Field(
        ...,
        alias="organization",
        title="Reference to the organization validating information",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization"],
    )
