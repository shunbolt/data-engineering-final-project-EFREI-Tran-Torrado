process_flask_credit=`netstat -tulnp | grep :5000 | cut -c81-`

process_id=`echo "$process_flask_credit" | tr -cd [:digit:]`

kill -9 $process_id
