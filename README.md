ISS Manifest Tracker 🛰️A production-ready, defensive Python backend script designed to poll real-time astronaut telemetry data directly from NASA's Open Notify API layers. This system implements secure network protocols and exception-handling frameworks to process global orbital datasets without application runtime failures.⚙️ Core Engineering FeaturesAPI Orchestration Layer: Dynamically fetches raw json telemetry payloads across live web servers.Defensive Exception Middleware: Implements custom try-except blocks to isolate validation failures and handle server timeouts elegantly without freezing execution loops.Scalable Data Mapping Matrix: Employs an automated for loop routing architecture that dynamically maps passenger manifests across shifting orbital vehicles.🛠️ System Architecture & Logic Flow[📡 Script Initialization]
           │
           ▼
[🌐 Knock on API Endpoint] ──► (Timeout / Offline) ──► [❌ Network Exception Message]
           │
     (Status 200 OK)
           │
           ▼
[💾 Parse JSON Memory Matrix] ──► (Broken Data Payload) ──► [🛑 Data Processing Safeguard]
           │
     (Validation Pass)
           │
           ▼
[🔄 Deploy Scalable For-Loop] ──► Iterates through array objects sequentially [ Box 0 ➡️ Box N ]
           │
           ▼
[🏁 Manifest Stream Rendered] ──► Terminal Outputs Clean, Uniquely Formatted Index
🚀 Execution Instructions1. PrerequisitesEnsure your local system architecture has Python 3.x installed along with the official web communication library:bashpip install requests
Use code with caution.2. Run the EngineExecute the tracking matrix via your local terminal line:bashpython day2.py
Use code with caution.📄 API Interface DocumentationThe script coordinates text requests through the following parameters:Target Data Node: http://open-notify.orgOutput Processing Profile:json{
  "number": 12,
  "people": [
    { "name": "Oleg Kononenko", "craft": "ISS" },
    { "name": "Nikolai Chub", "craft": "ISS" }
  ]
}
