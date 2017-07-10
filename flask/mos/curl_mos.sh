CURLFILE=curl_mos_list.txt
for URL in `cat $CURLFILE`
do
	echo $URL
	curl $URL
done
