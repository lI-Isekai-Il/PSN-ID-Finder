# PSN Online ID Finder 

**PSN Online ID Finder** is a fast, lightweight, and user-friendly desktop application designed to help users check the availability of PlayStation Network Online IDs—either individually or in bulk—through a clean interface and clear results.

The project emphasizes speed, clarity, and minimal overhead while maintaining a smooth workflow for both casual checks and long-running batch scans.

---

## Table of Contents

* [Features](#features)
* [Getting Started](#getting-started)
* [Usage](#usage)

  * [Check a Single ID](#check-a-single-id)
  * [Check Multiple IDs Using a File](#check-multiple-ids-using-a-file)
  * [Resume Interrupted Scans](#resume-interrupted-scans)
* [Output Formats](#output-formats)
  * [Available ID Lists](#available-id-lists)
  * [Ready-Made Input Files](#meady-made)
* [Releases](#releases)
* [License](#license)

---

## Features

* **Single ID Check**: Instantly verify whether a PSN Online ID is available, taken, or unavailable.
* **Bulk ID Scanning**: Load a `.txt` file containing multiple IDs and scan them automatically.
* **Live Progress Tracking**: Real-time counter showing checked IDs and the current ID being processed.
* **Resume Support**: Automatically detects unfinished scans and allows you to continue from where you stopped.
* **Multiple Save Formats**: Export available IDs as **JSON** or **TXT**.
* **Offline-Friendly Workflow**: Once started, scans can safely run for long periods (overnight usage supported).

---

## Getting Started

For the best experience, it is recommended to use the **precompiled Windows application**.

Download the latest version from the **Releases** section:

**Releases:** [Releases](https://github.com/lI-Isekai-Il/PSN-ID-Finder/releases)

Simply download, extract (if needed), and run the executable.

No Python installation is required when using the compiled version.

---

## Usage

### Check a Single ID

1. Launch the application.
2. Enter a PSN Online ID in the input field.
3. Click **CHECK** or press **Enter**.
4. The result will be displayed instantly:

   * **AVAILABLE** – The ID can be registered.
   * **TAKEN** – The ID is already in use.
   * **UNAVAILABLE** – The ID cannot be checked or is invalid.

---

### Check Multiple IDs Using a File

1. Prepare a `.txt` file.

   * Each PSN ID must be on a **separate line**.
2. Click **Select File**.
3. Choose your `.txt` file.
4. When prompted, select the save format:

   * **JSON** or **TXT**.
5. Choose the save location.
6. The scan will begin automatically.

During scanning, the application displays:

* Total checked IDs
* Currently processed ID
* Live progress updates

When finished, all available IDs will be saved to the selected file.

---

### Resume Interrupted Scans

If the application was closed or interrupted during a bulk scan:

* On the next launch, PSN Online ID Finder will detect the unfinished session.
* You will be prompted to **resume from the last checked ID**.
* Choose **YES**, then click **CHECK** again to continue.

This feature is ideal for long scans running overnight.

---

## Output Formats

### JSON Output

Each available ID is saved with metadata:

* `onlineId`
* `date` (UTC timestamp)

This format is recommended for automation, analysis, and future processing.

### TXT Output

* Plain list of available IDs
* Suitable for quick viewing and manual usage

---


### Available ID Lists (Ready-to-Use)

In addition to checking IDs manually or via your own files, you can also **browse and use pre-generated lists of available PSN Online IDs**.

All discovered available IDs are periodically organized and published inside a dedicated folder in the repository.

You can view them directly here:

**Available IDs Folder:**
 &nbsp;&nbsp; [Available PSN Online IDs](https://github.com/lI-Isekai-Il/PSN-ID-Finder/tree/main/Available%20IDs)

This allows you to:

* Quickly review already available Online IDs
* Avoid rescanning previously checked names
* Save time when searching for rare or clean IDs
  * **Availability lists are provided as-is and may change over time.**
---

### Ready-Made Input Files

For convenience, the project also provides **ready-to-use input files** containing curated PSN Online ID candidates.

These files are suitable for immediate use with the bulk scanning feature.

You can download and use them directly from here:

**Prepared Input Files:**
&nbsp;&nbsp;[Ready-to-Use ID Files](https://github.com/lI-Isekai-Il/PSN-ID-Finder/tree/main/IDs)

How to use :

1. Download any `.txt` file from the folder.
2. Open PSN Online ID Finder.
3. Select the downloaded file.
4. Choose your preferred output format.
5. Start scanning instantly.

This is especially useful for:

* New users
* Fast testing
* Large-scale scans without manual preparation

---

## Releases

All official builds are published here:

 [PSN ID Finder v1.03 & v1.05](https://github.com/lI-Isekai-Il/PSN-ID-Finder/releases/tag/App)

The project currently provides **two official editions**, each designed for a specific use case:

### 🔹 Normal Version — v1.03

* Standard and stable release
* Balanced performance and resource usage
* Recommended for most users
* Ideal for casual checks and normal batch scans

### ⚡ Faster Version — v1.05

* Optimized for higher speed and efficiency
* Improved performance for large ID lists
* Designed for long-running or heavy scans
* Recommended for advanced users

Each release includes:

* Versioned executable
* Changelog (when available)

Always download from the official repository to ensure authenticity and safety.

---

## License

This project is released under a **custom license** defined by the author.

* Personal, educational, and research use only
* No commercial usage
* No redistribution or rebranding
* No affiliation with Sony or PlayStation

Full license text is included inside the project.

---

Official Repository:
[PSN-ID-Finder](https://github.com/lI-Isekai-Il/PSN-ID-Finder)

---

Respect the code. Respect the author. Respect the license.
