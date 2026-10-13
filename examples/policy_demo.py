"""Offline teaching model only. No network, credentials, system changes or real authorization."""
import json
from pathlib import Path

def decide(r):
    if r.get("stop") or r.get("revoked"):
        return "DENY"
    if r.get("in_scope") is False or r.get("expired") is True:
        return "DENY"
    if r.get("tool_allowed") is False or r.get("action_allowed") is False:
        return "DENY"
    required = ("stop", "revoked", "in_scope", "expired", "tool_allowed",
                "action_allowed", "evidence_ok", "level")
    if any(k not in r for k in required):
        return "UNKNOWN"
    if any(type(r[k]) is not bool for k in required if k != "level"):
        return "UNKNOWN"
    if r["level"] not in ("A0", "A1", "A2", "A3", "A4"):
        return "UNKNOWN"
    if not r["evidence_ok"]:
        return "UNKNOWN"
    if r["level"] in ("A0", "A1"):
        return "ALLOW"
    if r["level"] == "A4":
        return "REVIEW"
    extra = ("preauthorized", "reversible", "critical", "recovery_ready")
    if any(k not in r or type(r[k]) is not bool for k in extra):
        return "UNKNOWN"
    if (not r["preauthorized"] or not r["reversible"] or
            r["critical"] or not r["recovery_ready"]):
        return "REVIEW"
    return "ALLOW"

def main():
    fixture = Path(__file__).with_name("policy-cases.json")
    cases = json.loads(fixture.read_text(encoding="utf-8"))
    results = []
    for case in cases:
        actual = decide(case["request"])
        results.append({"id": case["id"], "expected": case["expected"],
                        "actual": actual, "passed": actual == case["expected"]})
    report = {"mode": "offline-synthetic-only", "total": len(results),
              "passed": sum(x["passed"] for x in results), "results": results}
    print(json.dumps(report, ensure_ascii=False, indent=2))
    raise SystemExit(0 if report["passed"] == report["total"] else 1)

if __name__ == "__main__":
    main()

