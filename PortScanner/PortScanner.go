package main

import (
	"fmt"
	"net"
	"os"
	"strconv"
	"strings"
	"time"
)

const (
	defaultConnectTime = 500
)

func connetcToPort(id int, addr string, connectTime int, ch chan int) {
	startTime := time.Now()
	_, err := net.DialTimeout("tcp", addr, time.Millisecond*time.Duration(connectTime))
	time := time.Since(startTime).Milliseconds()

	if err != nil {
		// fmt.Printf("Ip addr:%s ERROR\r\n", ipAddr)
	} else {
		fmt.Printf("Ip addr:%s %dms OK\r\n", addr, time)
	}

	ch <- id
}

// go run main.go 192.168.150.1 22-500     300
//                IP seg        port       time
func main() {
	if len(os.Args) < 3 {
		fmt.Println("args error!")
	}

	fmt.Printf("---- Ip addr:%s:%s\r\n", os.Args[1], os.Args[2])

	ipSeg := os.Args[1]
	portSeg := os.Args[2]

	connectTime := (defaultConnectTime)
	if len(os.Args) > 3 {
		temp, err := strconv.Atoi(os.Args[3])
		if err == nil {
			connectTime = temp
		}
	}

	tempList := strings.Split(portSeg, "-")
	if len(tempList) != 2 {
		fmt.Printf("Port number error:%s\r\n", portSeg)
		os.Exit(1)
	}
	ch := make(chan int)
	startPort, startPortErr := strconv.Atoi(tempList[0])
	endPort, endPortErr := strconv.Atoi(tempList[1])

	if startPortErr == nil && endPortErr == nil && startPort > endPort {
		fmt.Printf("Port number error!\r\n")
		os.Exit(1)
	}

	for i := startPort; i < endPort; i++ {
		ipAddr := ipSeg + ":" + strconv.Itoa(i)
		go connetcToPort(i, ipAddr, connectTime, ch)
	}

	for i := startPort; i < endPort; i++ {
		<-ch
	}
}
