import React, { useState, useEffect } from 'react';
import Card from './Card';
import axios from 'axios';
// import { data } from './nr.json';
import Pagination from './Pagination';
import Spinner from './Spinner';

const Output = ({ cardInfo = [], query }) => {

    const [isLoading, setIsLoading] = useState(false);
    const [cardsData, setCardsData] = useState(cardInfo);
    const [currentPage, setCurrentPage] = useState(1);
    console.log(isLoading);

    useEffect(() => {
        if (query.length < 1) return;

        setIsLoading(true);
        axios.post(`http://127.0.0.1:5050/search_query`, { query: query, page: currentPage, page_count: 20 })
            .then(res => {
                setIsLoading(false);
                const result = [res.data.data[0]];
                if (result && result.length > 0) {
                    console.log(res.data);
                    // updateCardInfo(res.data.data);
                    setCardsData(res.data.data);
                    // setSymptoms();
                } else {
                    setCardsData([]);
                }
            }).catch(() => setIsLoading(false));
    }, [currentPage, query])

    return (
        <div>
            {isLoading && <Spinner className={'spinner-center'} />}
            {(!isLoading) && cardsData.length > 0 && <Pagination
                className="pagination-bar"
                currentPage={currentPage}
                onPageChange={page => setCurrentPage(page)}
            />}

            {(!isLoading) && cardsData.length > 0 &&
                cardsData.map((d, i) => (
                    <Card info={d} key={i}></Card>
                ))
            }

            {(!isLoading) && cardsData.length > 0 && <Pagination
                className="pagination-bar"
                currentPage={currentPage}
                onPageChange={page => setCurrentPage(page)}
            />}
        </div>

    );
};

export default Output;
