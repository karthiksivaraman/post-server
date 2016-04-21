# post-server
Python POST Server that accepts gzip files


Test using cURL

curl -X POST --data-binary @filename.txt.gz https://localhost:8443 -k --header "Content-Type:text/xml" --header "Content-Encoding:gzip" --header "X-filename:karthik.txt"
