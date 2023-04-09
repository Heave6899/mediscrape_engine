import React from 'react';
import LessText from './LessText';
const Card = ({ info }) => {
    let title, subtitle, content, symptoms, diseases, post_url;
    try {
        title = JSON.parse('"' + info.post_title[0].replace(/"/g, '\\"') + '"').replace(/%/g, '~~pct~~');
        title = decodeURIComponent(title).toString().replace(/~~pct~~/g, '%');

        subtitle = JSON.parse('"' + info.post_group[0].replace(/"/g, '\\"') + '"').replace(/%/g, '~~pct~~');
        subtitle = decodeURIComponent(subtitle).toString().replace(/~~pct~~/g, '%');

        post_url = info.post_url[0];
        content = JSON.stringify(info.post_content[0]);
        content = content.replace(/<[^>]+>/g, '');
        symptoms = info.symptoms;
        diseases = info.diseases;
    } catch (e) {
        console.log(e)
        console.log(info.post_content[0])
        console.log(JSON.parse('"' + info.post_title[0].replace(/"/g, '\\"') + '"'))
        console.log(info.post_group[0])
    }

    const openUrl = () => {
        window.open(
            post_url, "_blank");
    }


    return (
        <>
            {title &&
                <div className="cards">
                    <article className="information [ card ]">
                        <h2 className="title" onClick={openUrl}>{title}</h2>
                        <h2 className="subtitle">Group: {subtitle}</h2>
                        <LessText
                            text={content}
                            maxLength={300}
                        />

                        <div>
                            {symptoms &&
                                symptoms.length > 0 &&
                                <p className='heading'>Symptoms</p>}
                            {symptoms &&
                                symptoms.length > 0 &&
                                symptoms.map((s, i) => (
                                    <div key={i} className="chip">
                                        {s}
                                    </div>
                                ))
                            }
                        </div>

                        <div>
                            {diseases &&
                                diseases.length > 0 &&
                                <p className='heading'>Disease</p>}
                            {diseases &&
                                diseases.length > 0 &&
                                diseases.map((d, i) => (
                                    <div key={i} className="chip">
                                        {d}
                                    </div>
                                ))
                            }
                        </div>
                    </article>
                </div>
            }
        </>

    );
};

export default Card;

