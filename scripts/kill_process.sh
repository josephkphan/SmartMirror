echo "sudo netstat -tulpn | grep 5000"
output="$( sudo netstat -tulpn | grep 5000 )"

echo "${output}"
process_id="$( echo "$output" | sed -n 's/.*LISTEN      \(.*\)\/python.*/\1/p' )"

echo "kill ${process_id}"
kill $process_id