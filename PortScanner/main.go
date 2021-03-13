package main

import (
	"fmt"
	"net"
	"os"
	"strconv"
	"time"
)

const (
	defaultConnectTime = 500
)

func main() {
	if len(os.Args) < 3 {
		fmt.Println("args error!")
	}

	fmt.Printf("---- Ip addr:%s*:%s\r\n", os.Args[1], os.Args[2])

	ipSeg := os.Args[1]

	connectTime := (defaultConnectTime)
	if len(os.Args) > 3 {
		temp, err := strconv.Atoi(os.Args[3])
		if err == nil {
			connectTime = temp
		}
	}

	for i := 0; i < 255; i++ {
		ipAddr := ipSeg + strconv.FormatInt(int64(i), 10) + ":" + os.Args[2]

		startTime := time.Now()
		_, err := net.DialTimeout("tcp", ipAddr, time.Millisecond*time.Duration(connectTime))
		time := time.Since(startTime).Milliseconds()

		if err != nil {
			// fmt.Printf("Ip addr:%s ERROR\r\n", ipAddr)
		} else {
			fmt.Printf("Ip addr:%s %dms OK\r\n", ipAddr, time)
		}
	}
}
