import Header from "./component/Header"
import Footer from "./component/Footer"
import SearchBar from "./component/SearchBar"
import PaginationBar from "./component/PaginationBar"
import TableWrapper from "./component/TableWrapper"
import CreationModal from "./component/CreationModal";
import { useEffect, useState } from "react"

function App() {
  const [showCreation, setShowCreation] = useState(false)

  const CreateButtonHandler = () => {
    setShowCreation(true)
  }
  return (

    <>
      {showCreation && <CreationModal />}
      <Header />
      <main className="main">
        <section className="card users-container">
        <SearchBar />
        <TableWrapper />
        <button className="btn-add btn" onClick={CreateButtonHandler}>Add new user</button>
        <PaginationBar />
        </section>
      </main>
      <Footer />
    </>
  )
}

export default App
