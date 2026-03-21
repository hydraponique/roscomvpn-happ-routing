#!/usr/bin/env python3
"""
Generate QR codes for importing RoscomVPN geoasset URLs into v2RayNG.

Two QR codes are produced — one for geoip.dat and one for geosite.dat.
Users can scan these in v2RayNG -> Settings -> Geoasset update to
quickly set the correct geoasset URLs.

By default the stable GitHub Releases URLs are used: they always
point to the latest version and do not change. You can also pass
--source cdn to use the versioned jsdelivr CDN URLs from DEFAULT.JSON.

Dependencies: Python 3.8+, qrcode[pil]
    pip install qrcode[pil]
"""

import argparse
import json
import os
import sys
import urllib.request

try:
    import qrcode
except ImportError:
    print(
        "[!] 'qrcode' package is required.\n"
        "    Install it with:  pip install qrcode[pil]",
        file=sys.stderr,
    )
    sys.exit(1)

DEFAULT_CONFIG_URL = (
    "https://raw.githubusercontent.com/hydraponique/"
    "roscomvpn-routing/refs/heads/main/HAPP/DEFAULT.JSON"
)

# Stable URLs that always resolve to the latest release
RELEASES_URLS = {
    "geoip.dat": "https://github.com/hydraponique/roscomvpn-geoip/releases/latest/download/geoip.dat",
    "geosite.dat": "https://github.com/hydraponique/roscomvpn-geosite/releases/latest/download/geosite.dat",
}


def fetch_config(url: str) -> dict:
    """Download and parse the HAPP DEFAULT.JSON config."""
    print(f"[*] Fetching config from {url} ...")
    try:
        with urllib.request.urlopen(url) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except Exception as exc:
        print(f"[!] Failed to fetch config: {exc}", file=sys.stderr)
        sys.exit(1)


def get_urls(source: str, config_url: str) -> dict[str, str]:
    """Return geoasset URLs based on the chosen source."""
    if source == "releases":
        return dict(RELEASES_URLS)

    config = fetch_config(config_url)
    return {
        "geoip.dat": config.get("Geoipurl", RELEASES_URLS["geoip.dat"]),
        "geosite.dat": config.get("Geositeurl", RELEASES_URLS["geosite.dat"]),
    }


def generate_qr(data: str, output_path: str) -> None:
    """Generate a QR code PNG from a string."""
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(output_path)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate QR codes for v2RayNG geoasset URLs."
    )
    parser.add_argument(
        "--source",
        choices=["releases", "cdn"],
        default="releases",
        help=(
            "'releases' — stable GitHub Releases URLs (default). "
            "'cdn' — versioned jsdelivr CDN URLs from DEFAULT.JSON."
        ),
    )
    parser.add_argument(
        "--url",
        default=DEFAULT_CONFIG_URL,
        help="URL of the HAPP DEFAULT.JSON config (used with --source cdn).",
    )
    parser.add_argument(
        "-d", "--output-dir",
        default=".",
        help="Directory to save QR code images (default: current dir).",
    )
    args = parser.parse_args()

    urls = get_urls(args.source, args.url)

    os.makedirs(args.output_dir, exist_ok=True)

    for filename, url in urls.items():
        out_path = os.path.join(args.output_dir, f"{filename}.png")
        generate_qr(url, out_path)
        print(f"[+] {filename}: {os.path.abspath(out_path)}")
        print(f"    URL: {url}")

    print()
    print(
        "Scan these QR codes in v2RayNG -> Settings -> Geoasset update\n"
        "to set the correct geoasset download URLs."
    )


if __name__ == "__main__":
    main()
