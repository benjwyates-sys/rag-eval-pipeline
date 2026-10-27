"""Fetch the rag-eval-lab corpus from Wikipedia.

Downloads plain-text extracts for a curated list of autonomous-vehicle,
robotics, and perception topics and saves one Markdown file per article
under data/corpus/.

Wikipedia text is CC BY-SA 4.0; each file records its source URL.
Run:  python scripts/fetch_corpus.py
"""

import json
import re
import urllib.parse
import urllib.request
from pathlib import Path

API_URL = "https://en.wikipedia.org/w/api.php"
USER_AGENT = "rag-eval-lab/0.1 (portfolio project; https://github.com/benjwyates-sys)"
MAX_CHARS = 6000

TITLES = [
    # AV core
    "Autonomous car", "Self-driving car", "Waymo", "Zoox", "Cruise (autonomous vehicle)",
    "Tesla Autopilot", "Tesla Full Self-Driving", "Mobileye", "Aurora Innovation",
    "Motional", "Argo AI", "Pony.ai", "WeRide", "Baidu Apollo", "Nuro",
    "Kodiak Robotics", "TuSimple", "Gatik", "Torc Robotics",
    # Perception & sensing
    "Lidar", "Radar", "Computer vision", "Sensor fusion",
    "Simultaneous localization and mapping", "Kalman filter", "Particle filter",
    "Convolutional neural network", "Object detection", "Semantic segmentation",
    "Depth estimation", "Occupancy grid", "High-definition map",
    # Planning & control
    "Path planning", "Motion planning", "Control theory", "PID controller",
    "Model predictive control", "Operational design domain", "Geofence",
    # Safety & validation
    "ISO 26262", "Functional safety", "Safety of the intended functionality",
    "Validation and verification", "Safety case", "Redundancy (engineering)",
    "Fail-safe", "Automotive Safety Integrity Level",
    # Driver assistance & connectivity
    "Advanced driver-assistance system", "Lane departure warning system",
    "Adaptive cruise control", "Automatic emergency braking", "Blind spot monitor",
    "Vehicle-to-everything", "Dedicated short-range communications",
    # History
    "DARPA Grand Challenge", "Stanley (vehicle)", "History of self-driving cars",
    "SAE J3016",
    # Hardware & platforms
    "Nvidia Drive", "Luminar Technologies", "Velodyne Lidar",
    # ML fundamentals (for eval grounding)
    "Machine learning", "Deep learning", "Reinforcement learning",
    "Imitation learning", "Neural network", "Transformer (deep learning model)",
    "Attention (machine learning)", "Overfitting", "Ground truth",
    "Precision and recall", "Confusion matrix", "F1 score", "Receiver operating characteristic",
    "Cross-validation (statistics)", "Dataset", "Benchmark (computing)",
    # Society & policy
    "Autonomous vehicle liability", "Regulation of self-driving cars",
    "Ethics of artificial intelligence", "Trolley problem",
]


def slugify(title: str) -> str:
    slug = title.lower().replace(" ", "-")
    slug = re.sub(r"[^a-z0-9\-]", "", slug)
    return re.sub(r"-+", "-", slug).strip("-")


def fetch_one(title):
    """Fetch a single article. One title per request: batched extracts
    come back empty for most pages (TextExtracts quirk), so we go one by one."""
    params = {
        "action": "query",
        "prop": "extracts",
        "explaintext": 1,
        "redirects": 1,
        "titles": title,
        "format": "json",
        "formatversion": 2,
    }
    req = urllib.request.Request(
        API_URL + "?" + urllib.parse.urlencode(params),
        headers={"User-Agent": USER_AGENT},
    )
    with urllib.request.urlopen(req, timeout=60) as resp:
        return json.load(resp)


def trim(text: str) -> str:
    if len(text) <= MAX_CHARS:
        return text
    cut = text[:MAX_CHARS]
    # Prefer ending on a sentence boundary.
    last_period = cut.rfind(". ")
    if last_period > MAX_CHARS // 2:
        return cut[: last_period + 1]
    return cut


def main():
    out_dir = Path(__file__).resolve().parent.parent / "data" / "corpus"
    out_dir.mkdir(parents=True, exist_ok=True)
    fetched, missing = 0, []
    for title in TITLES:
        data = fetch_one(title)
        pages = data["query"]["pages"]
        page = pages[0] if pages else {}
        if "missing" in page:
            missing.append(title)
            continue
        canon = page["title"]
        body = trim(page.get("extract", "").strip())
        if not body:
            missing.append(title)
            continue
        slug = slugify(canon)
        url = "https://en.wikipedia.org/wiki/" + urllib.parse.quote(canon.replace(" ", "_"))
        text = f"# {canon}\n\n{body}\n\n---\nSource: {url} (CC BY-SA 4.0)\n"
        (out_dir / f"{slug}.md").write_text(text, encoding="utf-8")
        fetched += 1
    print(f"Fetched {fetched} articles into {out_dir}")
    if missing:
        print(f"Missing ({len(missing)}): {', '.join(missing)}")


if __name__ == "__main__":
    main()
