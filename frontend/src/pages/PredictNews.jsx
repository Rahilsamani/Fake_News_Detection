import { useState } from "react";
import axios from "axios";
import predictImage from "../assets/Images/predict.png";
import Footer from "../components/common/Footer";

function PredictNews() {
  const [inputText, setInputText] = useState("");
  const [prediction, setPrediction] = useState(null);
  const [loading, setLoading] = useState(false);

  const handlePredict = async () => {
    try {
      setLoading(true);
      const response = await axios.post(
        "https://7d85-2401-4900-5097-b055-ddd2-dcd3-5389-af91.ngrok-free.app/predict",
        {
          news: inputText,
        }
      );

      const predictedLabel = response.data.prediction;
      setPrediction(predictedLabel);

      // Save to DB
      await axios.post("http://localhost:5000/save-prediction", {
        news_text: inputText,
        predicted_label: predictedLabel,
        source_url: inputText.startsWith("http") ? inputText : null,
      });
    } catch (error) {
      console.error("Prediction Error:", error);
      setPrediction("Something went wrong.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <div className="grid min-h-[calc(100vh-3.5rem)] place-items-center bg-richblack-900 text-white">
        <div className="mx-auto flex w-10/12 max-w-maxContent flex-col-reverse justify-between gap-y-12 py-20 md:flex-row md:gap-x-12">
          {/* Left Section */}
          <div className="mx-auto w-11/12 max-w-[550px] md:mx-0">
            <h1 className="text-[1.875rem] font-semibold leading-[2.375rem] text-richblack-5">
              Predict News Authenticity
            </h1>
            <p className="mt-4 text-[1.125rem] leading-[1.625rem] text-richblack-200">
              Enter the news content or paste a URL below to check if it's real
              or fake.
            </p>

            <textarea
              rows={6}
              className="mt-6 w-full rounded-lg bg-richblack-700 p-4 text-white placeholder:text-richblack-300 outline-none resize-none"
              placeholder="Paste your news content or URL here..."
              value={inputText}
              onChange={(e) => setInputText(e.target.value)}
            />

            <button
              className="mt-4 w-full rounded-lg bg-blue-300 py-2 text-lg font-semibold text-white hover:bg-blue-400 transition-all duration-200"
              onClick={handlePredict}
              disabled={loading || inputText.trim() === ""}
            >
              {loading ? "Predicting..." : "Predict"}
            </button>

            {/* Result */}
            {prediction && !loading && (
              <div className="mt-6 text-xl font-bold text-center">
                Result:{" "}
                <span
                  className={`${
                    prediction.toLowerCase().includes("fake")
                      ? "text-red-500"
                      : "text-green-400"
                  }`}
                >
                  {prediction}
                </span>
              </div>
            )}
          </div>

          {/* Right Section - Image */}
          <div className="relative mx-auto w-11/12 max-w-[450px] md:mx-0 mt-10 md:mt-0">
            <img
              src={predictImage}
              alt="News Analysis"
              className="w-full"
              loading="lazy"
            />
          </div>
        </div>
      </div>
      <Footer />
    </div>
  );
}

export default PredictNews;
