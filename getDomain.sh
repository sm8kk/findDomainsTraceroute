# ./getDomain.sh <IP>

IP=$1
python getDomains.py $IP > temp.txt
cat temp.txt | tr -s " " |  tr "," "\n" | grep OrgId | cut -c 11- | rev | cut -c2- | rev

