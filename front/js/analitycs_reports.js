import React from "react";
import { createRoot } from "react-dom/client";
import Reports from "../components/analitycs/Reports";


(async function () {

    const rootContainer = document.getElementById('container');
    const root = createRoot(rootContainer);

    root.render(<Reports />);

})();
