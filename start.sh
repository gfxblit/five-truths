while true; do
    current_hour=$(date +%H)
    
    if [ $current_hour -ge 7 ] && [ $current_hour -lt 17 ]; then
			 	dotenv run python app.py
    fi
    
    sleep 10800
done
