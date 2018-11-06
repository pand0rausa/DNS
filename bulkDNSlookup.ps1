$computers = Get-Content C:\IPs.lst

workflow lookupparallel {
    param([string[]]$computers)
    ForEach -parallel($computer in $computers) {
    echo "Testing $computer"( 
    nslookup -timeout=1 -retry=1 $computer 208.67.220.220)
     }
     
 }


lookupparallel -computers $computers | out-file C:\lookup.txt
