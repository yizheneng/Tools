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

// go run main.go 192.168.150. 22     300
//                IP seg       port   time
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

	ch := make(chan int)
	for i := 0; i < 255; i++ {
		ipAddr := ipSeg + strconv.FormatInt(int64(i), 10) + ":" + os.Args[2]
		go connetcToPort(i, ipAddr, connectTime, ch)
	}

	for i := 0; i < 255; i++ {
		<-ch
	}
}
