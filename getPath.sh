#Usage: ./getPath.sh <dstIP>
dstIP=$1
tmpTraceRt="traceroute_tmp.txt"
path="path_to_"$dstIP".txt"
rm $path
traceroute $dstIP > $tmpTraceRt

wc_out=$(wc -l $tmpTraceRt)
length=($wc_out)

for i in `seq 2 ${length[0]}`; do
    #parse traceroute_tmp.txt to extract the IP addresses of the nodes/routers in the path
    IP=`cat $tmpTraceRt | awk 'NR == n' n=$i | cut -d "(" -f2 | cut -d ")" -f1`

    #for each IP address query the domain
    domain=`./getDomain.sh $IP`
    echo $domain
    echo $domain >> $path
done

X=`python domainHopsInPath.py $path`
echo "$dstIP,$X"
rm temp.txt
rm $tmpTraceRt
