(function () {
  console.log('ready!')
})

const postElements = document.getElementsByClassName('entry')

// postElements.map(entry => {
//   entry.addEventListener
// })
for (var i = 0; i < postElements.length; i++) {
  postElements[i].addEventListener('click', function () {
    const postId = this.getElementsByTagName('h2')[0].getAttribute('id')
    const node = this
    fetch(`/delete/${postId}`)
      .then(function (resp) {
        return resp.json()
      })
      .then(function (result) {
        if (result.status === 1) {
          node.parentNode.removeChild(node)
          console.log(result)
        }
        location.reload()
      })
      .catch(function (err) {
        console.log(err)
      })
  })
}