package main
import (
  "net/http"
  "strings"
)

var token = "loaderio-b1563d0e1a489bdfd2b21cc76d9b3c22"
func sendToken(w http.ResponseWriter, r *http.Request) {
  w.Write([]byte(token))
}

func sayHello(w http.ResponseWriter, r *http.Request) {
  message := r.URL.Path
  message = strings.TrimPrefix(message, "/")
  message = "Hello there " + message + "!!!"
  w.Write([]byte(message))
}

func main() {
  http.HandleFunc("/"+token+"/", sendToken)
  http.HandleFunc("/", sayHello)
  if err := http.ListenAndServe(":8080", nil); err != nil {
    panic(err)
  }
}
