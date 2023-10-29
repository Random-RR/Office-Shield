# OfficeShield Browser Extension

<img src="https://github.com/Random-RR/Office-Shield/blob/main/Extension/icons/icon.png" width="100" height="100" alt="OfficeShield Logo">

OfficeShield is a lightweight browser extension designed to help users analyze Microsoft Office files for potential threats and malware conveniently. It leverages the power of the VirusTotal API to provide quick and reliable analysis results. This extension is built to be user-friendly, making it easy to scan Office files directly from your browser.

## Features

- **Effortless Analysis**: Analyze Microsoft Office files (e.g., .docx, .xlsx, .pptx) with just a few clicks, directly from your browser.
- **VirusTotal Integration**: Leverages the VirusTotal API to check uploaded files for malicious content.
- **Real-time Updates**: Receive real-time analysis status and detailed results.
- **Easy Installation**: Simple installation process for popular web browsers.

## Installation

- Download the extension files (manifest.json, background scripts, etc.) from this repository.
- Open your Firefox browser.
- Enter `about:debugging` in the address bar and press Enter.
- Click on "This Firefox" in the left sidebar.
- Click on "Load Temporary Add-on" and select the `manifest.json` file from the downloaded extension files.

## Running the Backend Server (app.py)

To enable the full functionality of OfficeShield, you'll need to run the backend server (app.py) on your local machine. Here are the steps to do so:

1. Ensure you have Python and Flask installed on your system. If not, you can install Flask using `pip`:

   ```shell
   pip install flask

2. Edit the upload_headers variable in the code and change the VirusTotal API Key.

   upload_headers = { "x-apikey": "YOUR-VIRUSTOTAL-API-KEY"}
   
2. Run the command
   
   ```shell
   python3 app.py

## Usage

1. Click on the OfficeShield icon in your browser's toolbar.
2. Choose and upload the Office file you want to analyze.
3. OfficeShield will send the file to VirusTotal for analysis.
4. Monitor the analysis status and receive results in real-time.

## Requirements

- A supported web browser (e.g., Google Chrome, Mozilla Firefox).
- Internet connection to connect to VirusTotal API.
- VirusTotal API Key

## Disclaimer

OfficeShield is intended for educational and security analysis purposes. Use it responsibly and in compliance with applicable laws and regulations. The developers of OfficeShield are not responsible for any misuse of this tool.

## Contributing

We welcome contributions from the open-source community. Feel free to submit issues, feature requests, or pull requests to help improve OfficeShield.

## Author

- [Ravindu Rajasinghe](https://github.com/Random-RR)

---

## Disclaimer

**OfficeShield is intended solely for educational and security analysis purposes.** This project is designed to help users understand and explore the process of analyzing Microsoft Office files for potential threats and malware. It is not meant for any malicious or unethical use.

Please use OfficeShield responsibly and ensure that you comply with all applicable laws and regulations in your use of the tool. The developers of OfficeShield are not responsible for any misuse or illegal activities related to this tool.

