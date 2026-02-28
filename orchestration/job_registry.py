import uuid
import threading
from typing import Dict

from orchestration.contracts import GenerationInput
from orchestration.service import EvaluationService


class JobRegistry:

    def __init__(self):
        self._jobs: Dict[str, Dict] = {}
        self._lock = threading.Lock()
        self._service = EvaluationService()

    def submit(self, request: GenerationInput) -> str:
        job_id = str(uuid.uuid4())

        with self._lock:
            self._jobs[job_id] = {"status": "running", "result": None}

        thread = threading.Thread(
            target=self._execute,
            args=(job_id, request),
            daemon=True
        )
        thread.start()

        return job_id

    def _execute(self, job_id: str, request: GenerationInput):

        result = self._service.run(request)

        with self._lock:
            self._jobs[job_id] = {
                "status": "completed",
                "result": result
            }

    def status(self, job_id: str):
        with self._lock:
            return self._jobs.get(job_id, {"status": "not_found"})