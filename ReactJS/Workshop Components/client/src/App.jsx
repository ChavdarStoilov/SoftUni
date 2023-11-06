import Header from "./component/Header";
import Footer from "./component/Footer";
import MainSection from "./component/MainSection";

function App() {
    return (
        <>
        <Header />
        <main className="main">
            <MainSection />
        </main>
        <Footer />
        </>
    );
}

export default App;
