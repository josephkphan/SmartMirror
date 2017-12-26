
# takes port as command line argument
echo "sudo netstat -tulpn | grep $1"
output="$( sudo netstat -tulpn | grep $1 )"

echo "${output}"
process_id="$( echo "$output" | sed -n 's/.*LISTEN      \(.*\)\/python.*/\1/p' )"

echo "kill ${process_id}"
kill $process_id
