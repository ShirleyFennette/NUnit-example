using NUnit.Allure.Core;
using NUnit.Framework;

namespace Examples.Allure.NUnit.Test
{
    [AllureNUnit]
    class Tests
    {
        [Test]
        public void Test1()
        {
            Assert.Pass();
        }
    }
}