import asyncio
import time

from fastapi import FastAPI

app = FastAPI(title="Async Service Dashboard")


async def fetch_inventory() -> dict[str, str]:
    # TODO: Simulate an I/O operation and return the inventory service status.
    raise NotImplementedError


async def fetch_shipping() -> dict[str, str]:
    # TODO: Simulate an I/O operation and return the shipping service status.
    raise NotImplementedError


async def fetch_payments() -> dict[str, str]:
    # TODO: Simulate an I/O operation and return the payments service status.
    raise NotImplementedError


@app.get("/dashboard")
async def read_dashboard() -> dict[str, list[dict[str, str]]]:
    # TODO: Use asyncio.gather to collect all service results concurrently.
    return {"services": []}


@app.get("/dashboard/sequential")
async def read_dashboard_sequential() -> dict[str, object]:
    start_time = time.perf_counter()

    # TODO: Await each service one at a time and collect the results.
    services: list[dict[str, str]] = []

    duration = time.perf_counter() - start_time
    return {"services": services, "duration_seconds": round(duration, 2)}
