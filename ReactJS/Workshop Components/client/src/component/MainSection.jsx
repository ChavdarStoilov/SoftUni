import SearchBar from "./SearchBar";
import PaginationBar from "./PaginationBar";
import TableWrapper from "./TableWrapper";
import CreationModal from "./CreationModal";
import { useEffect, useState } from "react";

export default function MainSection() {
    const [showCreation, setShowCreation] = useState(false);

    const CreateButtonHandler = () => {
        setShowCreation(true);
    };    

    const OnClose = () => {
        setShowCreation(false)
    };

    return (
        <section className="card users-container">
           {showCreation && <CreationModal 
            onClose ={OnClose}      
            />}
        <SearchBar />
        <TableWrapper />
        <button className="btn-add btn" onClick={CreateButtonHandler}>
            Add new user
        </button>
        <PaginationBar />
        </section>
    )
}