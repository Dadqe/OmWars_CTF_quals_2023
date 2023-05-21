using System.Security.Cryptography;
using System.Text;
using BCrypt.Net;
using Miner.Views;

namespace Miner.Services
{
    public class MiningService
    {
        private const int MIN_STRING = 16;
        private const int MAX_STRING = 32;
        private const int SHRINK = 3;
        public readonly int TIMES_TO_SOLVE;

        private int _solved = 0;
        private MiningData? _lastSend;
        private string _flag;

        private readonly Random _random;

        public MiningService()
        {
            _flag = Environment.GetEnvironmentVariable("FLAG") ?? "Flag error, contact with support";

            _random = new Random();

            TIMES_TO_SOLVE = 30 + (DateTime.UtcNow.Hour - 6) * 5;
        }

        public MiningData GenerateNextString()
        {
            if (_lastSend != null) return _lastSend.Value;

            string String = "";

            int length = _random.Next(MIN_STRING, MAX_STRING + 1);

            for (int i = 0; i < length; i++)
            {
                char nextChar = (char)_random.Next(65, 91);

                String += nextChar;
            }

            string Hash = BCrypt.Net.BCrypt.HashPassword(String, 4); 
            Console.WriteLine(String);

            _lastSend = new MiningData { MiningString = String.Substring(0, String.Length - SHRINK), Length = length, Hash = Hash };

            return _lastSend.Value;
        }

        public string ApproveString(string String)
        {
            if (_lastSend == null) return "";

            if (BCrypt.Net.BCrypt.Verify(String, _lastSend.Value.Hash))
            {
                _solved++;
                _lastSend = null;

                if (_solved >= TIMES_TO_SOLVE) return $"Mandalorean, you have redeemed yourself. We forgive you! Hold your flag: {_flag}";

                return $"Solved {_solved}/{TIMES_TO_SOLVE}";
            }

            _lastSend = null;
            _solved = 0;
            return $"Solved {_solved}/{TIMES_TO_SOLVE}";
        }
    }
}
