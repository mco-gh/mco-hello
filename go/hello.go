package main
import (
  "fmt"
  "math/rand"
  "net/http"
  "strings"
  "time"
)

var token = "loaderio-b1563d0e1a489bdfd2b21cc76d9b3c22"
func sendToken(w http.ResponseWriter, r *http.Request) {
  w.Write([]byte(token))
}

func sayHello(w http.ResponseWriter, r *http.Request) {
  path := strings.TrimPrefix(r.URL.Path, "/")
  if path == "" {
    path = "World"
  }
  random := rand.Intn(16777215)
  color := fmt.Sprintf("%6.6x", random)
  style := "style=\"background-color:#" + color + "\""
  message := "<h1 " + style + ">Hello " + path + "!!!</h1>"
  w.Write([]byte(message))
}

func main() {
  rand.Seed(time.Now().UTC().UnixNano())
  http.HandleFunc("/"+token+"/", sendToken)
  http.HandleFunc("/", sayHello)
  if err := http.ListenAndServe(":8080", nil); err != nil {
    panic(err)
  }
}
