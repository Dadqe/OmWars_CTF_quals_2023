using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;

using Miner.Services;
using Miner.Views;

namespace Miner.Controllers
{
    [Route("/")]
    [ApiController]
    public class MiningController : ControllerBase
    {
        private readonly MiningService _miningService;

        public MiningController(MiningService miningService)
        {
            _miningService = miningService;
        }

        [HttpGet]
        public MiningData GetNext()
        {
            return _miningService.GenerateNextString();
        }

        [HttpPost]
        public string Approve(string String)
        {
            return _miningService.ApproveString(String);
        }

        [Route("/info")]
        public string GetInfo() => 
 
            "You came this ctf without the helmet?! Unforgivable!!\nNow thouse mines is your new home!\n\n" +
            "Well, as a fellow I give you a little advice:\nYou will get a strange structure and your first question is \"what should I do with this staff?\"\n" +
            "Don`t worry, it has 3 parts: {part of an ancient code,   initial length of it,   and a BCrypt hash of full code}\n" +
            "The only thing you should send is original code... Or something what would have the same hash\n" +
            "You can use first two parts or comepletely skip that, it`s only a hint...\n\n" +
            $"It`s time to work sinner. Make it {_miningService.TIMES_TO_SOLVE} times and you will free";
    }
}
