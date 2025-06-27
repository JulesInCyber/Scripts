#!/bin/bash

: '
This script can be used to find binaries that have a misconfigured SUID bit.
The array _vulnbins_ can be extended with other binaries, that have a SUID-vulnerability
You can chek GTFObins for other.
'

RED="\e[1;91m"
YEL="\e[1;93m"
RESET="\e[0m"

echo -e "${YEL}[~] Checking for set SUID-Bits for user root${RESET}"

find / -user root -perm /4000 2>/dev/null | sort

echo -e "\n[!] Checking known vulnerabilities"
vulnbins=(bash perl python find vim nmap cp tar nano less more file date diff ip gzip mv tee time wget ssh-keygen)

for bin in "${vulnbins[@]}"; do
    which $bin &>/dev/null && \
    find $(which $bin) -user root -perm -4000 -exec echo -e "${RED}[!] $bin has a SUID bit set${RESET}" \;
done

echo -e "\n[!] Done"
