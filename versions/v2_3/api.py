"""OCPI Versions API endpoints."""
from datetime import datetime, timezone
from typing import List
from fastapi import APIRouter, Request
from pydantic import HttpUrl

from versions.v2_3.schemas import (
    Version,
    VersionDetail,
    VersionNumber,
    OCPIResponse,
    Endpoint,
    ModuleID,
    InterfaceRole
)

router = APIRouter(
    prefix="/ocpi/emsp/versions",
    tags=["Versions"],
    responses={404: {"description": "Not found"}},
)


def get_base_url(request: Request) -> str:
    """Get base URL from request."""
    return f"{request.url.scheme}://{request.url.netloc}"


def create_ocpi_response(data, status_code: int = 1000, status_message: str = "Success") -> OCPIResponse:
    """Create a standard OCPI response."""
    return OCPIResponse(
        data=data,
        status_code=status_code,
        status_message=status_message,
        timestamp=datetime.now(timezone.utc).isoformat()
    )


@router.get(
    "",
    response_model=OCPIResponse,
    summary="List available OCPI versions",
    description="Returns a list of all OCPI versions supported by this eMSP implementation."
)
async def get_versions(request: Request) -> OCPIResponse:
    """
    GET /ocpi/emsp/versions
    
    Returns all available OCPI versions. This is the entry point for OCPI communication.
    """
    base_url = get_base_url(request)
    
    versions: List[Version] = [
        Version(
            version=VersionNumber.V2_3,
            url=HttpUrl(f"{base_url}/ocpi/emsp/versions/2.3")
        )
    ]
    
    return create_ocpi_response(versions)


@router.get(
    "/2.3",
    response_model=OCPIResponse,
    summary="Get OCPI 2.3 version details",
    description="Returns detailed information about OCPI version 2.3 including available endpoints."
)
async def get_version_details(request: Request) -> OCPIResponse:
    """
    GET /ocpi/emsp/versions/2.3
    
    Returns version details including all available endpoints for OCPI 2.3.
    """
    base_url = get_base_url(request)
    
    # Define available endpoints for eMSP
    endpoints: List[Endpoint] = [
        Endpoint(
            identifier=ModuleID.CREDENTIALS,
            role=InterfaceRole.RECEIVER,
            url=HttpUrl(f"{base_url}/ocpi/emsp/2.3/credentials")
        ),
        Endpoint(
            identifier=ModuleID.LOCATIONS,
            role=InterfaceRole.RECEIVER,
            url=HttpUrl(f"{base_url}/ocpi/emsp/2.3/locations")
        ),
        Endpoint(
            identifier=ModuleID.SESSIONS,
            role=InterfaceRole.RECEIVER,
            url=HttpUrl(f"{base_url}/ocpi/emsp/2.3/sessions")
        ),
        Endpoint(
            identifier=ModuleID.CDRS,
            role=InterfaceRole.RECEIVER,
            url=HttpUrl(f"{base_url}/ocpi/emsp/2.3/cdrs")
        ),
        Endpoint(
            identifier=ModuleID.TARIFFS,
            role=InterfaceRole.RECEIVER,
            url=HttpUrl(f"{base_url}/ocpi/emsp/2.3/tariffs")
        ),
        Endpoint(
            identifier=ModuleID.TOKENS,
            role=InterfaceRole.SENDER,
            url=HttpUrl(f"{base_url}/ocpi/emsp/2.3/tokens")
        ),
        Endpoint(
            identifier=ModuleID.COMMANDS,
            role=InterfaceRole.SENDER,
            url=HttpUrl(f"{base_url}/ocpi/emsp/2.3/commands")
        ),
        Endpoint(
            identifier=ModuleID.CHARGING_PROFILES,
            role=InterfaceRole.SENDER,
            url=HttpUrl(f"{base_url}/ocpi/emsp/2.3/chargingprofiles")
        ),
    ]
    
    version_detail = VersionDetail(
        version=VersionNumber.V2_3,
        endpoints=endpoints
    )
    
    return create_ocpi_response(version_detail)
