// Fetch prints the content found at a URL.
package main

import (
	"fmt"
	"io/ioutil"
	"net/http"
	"os"
	"time"
)

func main() {
	start := time.Now()
	for _, url := range os.Args[1:] {
		reqStart := time.Now()
		resp, err := http.Get(url)
		if err != nil {
			fmt.Fprintf(os.Stderr, "fetch: %v\n", err)
			os.Exit(1)
		}
		b, err := ioutil.ReadAll(resp.Body)
		resp.Body.Close()
		if err != nil {
			fmt.Fprintf(os.Stderr, "fetch: reading %s: %v\n", url, err)
			os.Exit(1)
		}
		reqSecs := time.Since(reqStart).Seconds()
		//fmt.Printf("%s", b)
		nbytes := len(b)
		fmt.Printf("%.2fs %7d %s\n", reqSecs, nbytes, url)
	}
	fmt.Printf("\n%.2fs elapsed\n", time.Since(start).Seconds())
}
