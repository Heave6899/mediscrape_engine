import React, { useState, useEffect } from 'react';
import axios from 'axios';
import useClickOutside from '../hooks/useClickOutside';
import RedSpinner from './RedSpinner';


const SearchBar = ({ updateQuery }) => {
    const [isLoading, setIsLoading] = useState(false);
    const [searchInput, setSearchInput] = useState('');
    const [isSuggestionActive, setIsSuggestionActive] = useState('');
    const [suggestions, setSuggestions] = useState([]);
    const [selections, setSelections] = useState([]);
    const [symptoms, setSymptoms] = useState([]);
    const [diseases, setDiseases] = useState([]);

    let domNode = useClickOutside(() => {
        setIsSuggestionActive('');
    });

    useEffect(() => {
        if (searchInput.length < 5) {
            setIsSuggestionActive('');
            return;
        }
        setIsSuggestionActive('active');
        const delayDebounceFn = setTimeout(() => {

            setIsLoading(true);
            axios.get(`http://127.0.0.1:5050/auto_complete?q=${searchInput}`).then(function (response) {

                const result = response.data.syos;
                setIsLoading(false);
                if (result && result.length > 0) {
                    setSuggestions(result);
                }



            }).catch(function (error) {
                setIsLoading(false);
                console.log(error)
            });
        }, 1000)

        return () => clearTimeout(delayDebounceFn)
    }, [searchInput])

    const selectOption = (suggestion) => {
        if (!(selections.indexOf(suggestion) > -1)) {
            setSelections([...selections, suggestion]);
        }
    }

    const removeOption = (selection) => {
        setSelections(selections.filter((item) => item !== selection));
    }

    const searchResult = () => {

        if (searchInput && searchInput.length > 0 && selections.indexOf(searchInput) < 0) setSelections([...selections, searchInput]);

        setSearchInput('');

        const req = {
            query: selections.join(', '),
            page: 1,
            page_count: 20
        };
        updateQuery(selections.join(', '));

        setIsLoading(true);
        axios.post(`http://127.0.0.1:5050/search_query`, req)
            .then(res => {
                setIsLoading(false);
                // console.log(res);
                const result = [res.data.data[0]];
                if (result && result.length > 0) {
                    console.log(res.data);
                    // updateCardInfo(res.data.data);
                    setSymptoms(res.data.syos);
                    setDiseases(res.data.disea);
                    // setSymptoms();
                } else {
                    setSymptoms([]);
                    setDiseases([]);
                }
            }).catch(() => setIsLoading(false));
    }

    return (
        <>
            <div className='title' style={{ 'color': '#cc0000', marginBottom: '10px', fontSize: '2rem', textAlign: 'center' }}>Mediscrape</div>

            <div className={`searchInput ${isSuggestionActive}`}>

                <input
                    type="text"
                    value={searchInput}
                    onChange={(e) => setSearchInput(e.target.value)}
                    placeholder="Enter.." />
                <span className="icon" onClick={searchResult}>🔍</span>

                <div className="resultBox" ref={domNode}>
                    <li onClick={() => selectOption(searchInput)} key='-1'>{searchInput}</li>
                    <li style={{ marginTop: '5px', fontSize: '12px', fontWeight: '200' }}>Suggestions</li>
                    {isLoading && <li style={{ padding: '40px 0' }} onClick={() => selectOption(searchInput)} key='-2'><RedSpinner /></li>}
                    {(!isLoading) && suggestions.map((suggestion, i) => (<li onClick={() => selectOption(suggestion)} key={i}>{suggestion}</li>))}
                </div>

            </div>

            {selections.map((selection, i) => (
                <div key={i} className="chip">
                    {selection}
                    <span className="closebtn" onClick={() => removeOption(selection)}>&times;</span>
                </div>
            ))}

            {(symptoms.length > 0 || diseases.length > 0) &&
                <div className='cards' style={{ marginTop: '50px' }}>
                    <article className="information [ card ]">
                        <div>
                            <p className='heading'>Top Symptoms</p>
                            {
                                symptoms.length > 0 &&
                                symptoms.map((s, i) => (
                                    <div onClick={() => selectOption(s)} key={i} className="chip">
                                        {s}
                                    </div>
                                ))
                            }
                        </div>

                        <div>
                            <p className='heading'>Top Diseases</p>
                            {
                                diseases.length > 0 &&
                                diseases.map((d, i) => (
                                    <div onClick={() => selectOption(d)} key={i} className="chip">
                                        {d}
                                    </div>
                                ))
                            }
                        </div>
                    </article>
                </div>}



        </>
    );
};

export default SearchBar;