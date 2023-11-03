import TableWrapper from "./TableWrapper";

export default function Main() {
    
    return (
        <div>
            <section className="todo-list-container">
              <h1>Todo List</h1>

              <div className="add-btn-container">
                <button className="btn">+ Add new Todo</button>
              </div>

              <TableWrapper />
            </section>
        </div>
    );
}