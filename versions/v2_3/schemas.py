"""Pydantic schemas for OCPI Versions endpoint."""
from typing import List, Optional, Union
from pydantic import BaseModel, Field, HttpUrl
from enum import Enum


class InterfaceRole(str, Enum):
    """The role of the party in the OCPI network."""
    SENDER = "SENDER"
    RECEIVER = "RECEIVER"


class ModuleID(str, Enum):
    """Identifiers for OCPI modules."""
    CDRS = "cdrs"
    CHARGING_PROFILES = "chargingprofiles"
    COMMANDS = "commands"
    CREDENTIALS = "credentials"
    HUB_CLIENT_INFO = "hubclientinfo"
    LOCATIONS = "locations"
    SESSIONS = "sessions"
    TARIFFS = "tariffs"
    TOKENS = "tokens"


class Endpoint(BaseModel):
    """Details of one endpoint for a specific OCPI module."""
    
    identifier: ModuleID = Field(
        ...,
        description="Endpoint identifier"
    )
    role: InterfaceRole = Field(
        ...,
        description="Interface role this endpoint implements"
    )
    url: HttpUrl = Field(
        ...,
        description="URL to this endpoint"
    )

    class Config:
        json_schema_extra = {
            "example": {
                "identifier": "locations",
                "role": "RECEIVER",
                "url": "https://example.com/ocpi/emsp/2.3/locations"
            }
        }


class VersionNumber(str, Enum):
    """OCPI version numbers."""
    V2_0 = "2.0"
    V2_1 = "2.1"
    V2_1_1 = "2.1.1"
    V2_2 = "2.2"
    V2_2_1 = "2.2.1"
    V2_3 = "2.3"


class Version(BaseModel):
    """Contains information about a version of the OCPI protocol."""
    
    version: VersionNumber = Field(
        ...,
        description="The version number"
    )
    url: HttpUrl = Field(
        ...,
        description="URL to the version details endpoint"
    )

    class Config:
        json_schema_extra = {
            "example": {
                "version": "2.3",
                "url": "https://example.com/ocpi/emsp/versions/2.3"
            }
        }


class VersionDetail(BaseModel):
    """Contains version details and available endpoints."""
    
    version: VersionNumber = Field(
        ...,
        description="The version number"
    )
    endpoints: List[Endpoint] = Field(
        ...,
        description="A list of supported endpoints for this version"
    )

    class Config:
        json_schema_extra = {
            "example": {
                "version": "2.3",
                "endpoints": [
                    {
                        "identifier": "credentials",
                        "role": "RECEIVER",
                        "url": "https://example.com/ocpi/emsp/2.3/credentials"
                    },
                    {
                        "identifier": "locations",
                        "role": "RECEIVER",
                        "url": "https://example.com/ocpi/emsp/2.3/locations"
                    }
                ]
            }
        }


class OCPIResponse(BaseModel):
    """Standard OCPI response wrapper."""
    
    data: Optional[Union[Version, List[Version], VersionDetail]] = Field(
        None,
        description="The actual response data"
    )
    status_code: int = Field(
        ...,
        description="OCPI status code",
        ge=1000,
        le=3999
    )
    status_message: Optional[str] = Field(
        None,
        description="Optional status message"
    )
    timestamp: str = Field(
        ...,
        description="Timestamp of the response in RFC3339 format"
    )

    class Config:
        json_schema_extra = {
            "example": {
                "data": [
                    {
                        "version": "2.3",
                        "url": "https://example.com/ocpi/emsp/versions/2.3"
                    }
                ],
                "status_code": 1000,
                "status_message": "Success",
                "timestamp": "2025-11-02T12:00:00Z"
            }
        }
