from fastapi import Request
import time

async def track_request_metrics(request: Request, call_next):
    start = time.monotonic()
    response = await call_next(request)
    duration_ms = (time.monotonic() - start) * 1000
    print(f"[metrics] {request.method} {request.url.path} {response.status_code} {duration_ms:.1f}ms")
    return response
