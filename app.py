from flask import Flask, request, render_template
import requests
import time

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        # Handle file upload
        uploaded_file = request.files["file"]
        if uploaded_file.filename != "":
            allowed_extensions = {'docx', 'xlsx', 'pptx'}
            file_extension = uploaded_file.filename.split('.')[-1].lower()
            if file_extension in allowed_extensions:
                # Step 1: Upload the file to VirusTotal
                upload_url = "https://www.virustotal.com/api/v3/files"
                upload_headers = {
                    "x-apikey": "YOUR-VIRUSTOTAL-API-KEY"
                }

                files = {"file": (uploaded_file.filename, uploaded_file.stream)}

                upload_response = requests.post(upload_url, files=files, headers=upload_headers)

                if upload_response.status_code == 200:
                    upload_data = upload_response.json()
                    file_id = upload_data['data']['id']

                    # Step 2: Wait for analysis to complete
                    analysis_url = f"https://www.virustotal.com/api/v3/analyses/{file_id}"
                    analysis_headers = {
                        "x-apikey": "YOUR-VIRUSTOTAL-API-KEY"
                    }

                    while True:
                        analysis_response = requests.get(analysis_url, headers=analysis_headers)
                        if analysis_response.status_code == 200:
                            analysis_data = analysis_response.json()
                            attributes = analysis_data['data']['attributes']
                            status = attributes['status']

                            if status == 'completed':
                                results = {
                                    'suspicious': attributes['stats']['suspicious'],
                                    'malicious': attributes['stats']['malicious'],
                                    'undetected': attributes['stats']['undetected']
                                }
                                return render_template("result.html", results=results)
                            else:
                                analysis_status = f"Analysis status: {status}. Waiting for analysis to complete..."
                                time.sleep(10)  # Wait for 10 seconds before checking again
                                return render_template("upload.html", analysis_status=analysis_status)
                        else:
                            error_message = f"Failed to get analysis results. Status code: {analysis_response.status_code}"
                            return render_template("upload.html", error_message=error_message)

                else:
                    error_message = f"Failed to upload the file. Status code: {upload_response.status_code}"
                    return render_template("upload.html", error_message=error_message)
            else:
                error_message = "Unsupported file type. Please upload a Word, Excel, or PowerPoint file."
                return render_template("upload.html", error_message=error_message)

    return render_template("upload.html")

if __name__ == "__main__":
    app.run(debug=True)
