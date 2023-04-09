import React from 'react';

const LessText = ({ text, maxLength }) => {

    const [hidden, setHidden] = React.useState(true);
    // try {
    //     text = decodeURIComponent(text);
    // } catch (e) {
    //     console.log(text)
    //     console.log(e);
    // }

    if (text.length <= maxLength) {
        return <div className="info">{text}</div>;
    }

    return (
        <div className="info">
            {hidden
                ? `${text.substr(0, maxLength).trim()}...`
                : text
            }
            {hidden
                ? (<a href="/#" className="link" onClick={() => setHidden(false)}> read more</a>)
                : (<a href="/#" className="link" onClick={() => setHidden(true)}> read less</a>)
            }
        </div>
    );
}

export default LessText;