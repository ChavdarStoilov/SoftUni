import Header from "./component/Header"
import Footer from "./component/Footer"
import SearchBar from "./component/SearchBar"
import PaginationBar from "./component/PaginationBar"
import TableWrapper from "./component/TableWrapper"


function App() {

  return (
    <>
      <Header />
      <main className="main">
        <section className="card users-container">
        <SearchBar />
        <TableWrapper />
        <PaginationBar />
        <button className="btn-add btn">Add new user</button>
        </section>
      </main>
      <Footer />
    </>
  )
}

export default App
